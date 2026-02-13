"""
ComOS Federation Gateway — LangChain Shopping Agent

A LangChain agent that connects to the ComOS Federation Gateway
and can browse stores, search products, and manage a shopping cart.
"""

import asyncio
import json
from mcp import ClientSession
from mcp.client.sse import sse_client
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import StructuredTool
from langchain_core.prompts import ChatPromptTemplate

GATEWAY_URL = "https://mcp.comos-gateway.com/mcp/sse"

SHOPPING_TASK = "Find running shoes under $150 on any available store and add the best option to my cart"


def make_langchain_tool(session, mcp_tool):
    """Convert an MCP tool to a LangChain StructuredTool."""

    async def call_tool(**kwargs):
        result = await session.call_tool(mcp_tool.name, kwargs)
        return result.content[0].text

    return StructuredTool.from_function(
        coroutine=call_tool,
        name=mcp_tool.name,
        description=mcp_tool.description or mcp_tool.name,
        args_schema=None,
    )


async def main():
    print("Connecting to ComOS Federation Gateway...")

    async with sse_client(GATEWAY_URL) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            # Load MCP tools as LangChain tools
            mcp_tools = await session.list_tools()
            tools = [make_langchain_tool(session, t) for t in mcp_tools.tools]
            print(f"Loaded {len(tools)} ComOS tools into LangChain")

            # Create the agent
            llm = ChatOpenAI(model="gpt-4o", temperature=0)
            prompt = ChatPromptTemplate.from_messages([
                ("system", (
                    "You are a shopping assistant with access to the ComOS "
                    "Federation Gateway. You can discover stores, search products, "
                    "manage a cart, and complete purchases. Always start by listing "
                    "available tenants to find stores, then search within them."
                )),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ])

            agent = create_tool_calling_agent(llm, tools, prompt)
            executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

            # Run the shopping task
            print(f"\nTask: {SHOPPING_TASK}\n")
            result = await executor.ainvoke({"input": SHOPPING_TASK})
            print(f"\nResult: {result['output']}")


if __name__ == "__main__":
    asyncio.run(main())
