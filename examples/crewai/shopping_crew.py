"""
ComOS Federation Gateway — CrewAI Shopping Crew

A multi-agent crew that discovers stores, searches products,
manages a cart, and completes purchases via the ComOS Federation Gateway.
"""

import asyncio
import json
from mcp import ClientSession
from mcp.client.sse import sse_client
from crewai import Agent, Task, Crew, Process
from langchain.tools import StructuredTool

GATEWAY_URL = "https://mcp.comos-gateway.com/mcp/sse"

SHOPPING_REQUEST = "Find the best running shoes under $150 and add them to my cart"


def make_langchain_tool(session, mcp_tool):
    """Convert an MCP tool to a LangChain-compatible tool for CrewAI."""

    async def call_tool(**kwargs):
        result = await session.call_tool(mcp_tool.name, kwargs)
        return result.content[0].text

    def call_tool_sync(**kwargs):
        return asyncio.get_event_loop().run_until_complete(call_tool(**kwargs))

    return StructuredTool.from_function(
        func=call_tool_sync,
        name=mcp_tool.name,
        description=mcp_tool.description or mcp_tool.name,
    )


async def main():
    print("Connecting to ComOS Federation Gateway...")

    async with sse_client(GATEWAY_URL) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            # Load MCP tools
            mcp_tools = await session.list_tools()
            all_tools = [make_langchain_tool(session, t) for t in mcp_tools.tools]
            print(f"Loaded {len(all_tools)} ComOS tools")

            # Partition tools by role
            discovery_tools = [t for t in all_tools if t.name.startswith(("federation_", "catalog_"))]
            cart_tools = [t for t in all_tools if t.name.startswith(("cart_", "catalog_"))]
            checkout_tools = [t for t in all_tools if t.name.startswith(("checkout_", "cart_", "orders_"))]

            # Define agents
            store_scout = Agent(
                role="Store Scout",
                goal="Discover available stores and find the best products matching the shopping request",
                backstory="You are an expert product researcher with access to the ComOS commerce network. You know how to find the best deals across multiple stores.",
                tools=discovery_tools,
                verbose=True,
            )

            cart_manager = Agent(
                role="Cart Manager",
                goal="Select the best products from the research results and add them to the shopping cart",
                backstory="You are a shopping assistant who picks the best options and manages the cart efficiently.",
                tools=cart_tools,
                verbose=True,
            )

            checkout_agent = Agent(
                role="Checkout Coordinator",
                goal="Review the cart and prepare for checkout",
                backstory="You are a purchase coordinator who ensures the cart is correct before initiating checkout.",
                tools=checkout_tools,
                verbose=True,
            )

            # Define tasks
            research_task = Task(
                description=f"Research products for this request: {SHOPPING_REQUEST}. Start by listing available stores with federation_list_tenants, then search for products with catalog_search.",
                expected_output="A list of matching products with names, prices, and tenant IDs",
                agent=store_scout,
            )

            cart_task = Task(
                description="Based on the research results, add the best product(s) to the cart using cart_add_item. Then verify the cart with cart_view.",
                expected_output="Cart contents showing the selected items",
                agent=cart_manager,
            )

            review_task = Task(
                description="Review the cart contents and provide a summary. If everything looks good, indicate the cart is ready for checkout.",
                expected_output="Final cart review with total price and confirmation",
                agent=checkout_agent,
            )

            # Run the crew
            crew = Crew(
                agents=[store_scout, cart_manager, checkout_agent],
                tasks=[research_task, cart_task, review_task],
                process=Process.sequential,
                verbose=True,
            )

            print(f"\nShopping request: {SHOPPING_REQUEST}\n")
            result = crew.kickoff()
            print(f"\nFinal result:\n{result}")


if __name__ == "__main__":
    asyncio.run(main())
