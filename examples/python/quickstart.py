"""
ComOS Federation Gateway — Python Quickstart

Connects to the ComOS Federation Gateway via MCP SSE,
lists available merchants, and searches for products.
"""

import asyncio
import json
from mcp import ClientSession
from mcp.client.sse import sse_client

GATEWAY_URL = "https://mcp.comos-gateway.com/mcp/sse"


async def main():
    print("Connecting to ComOS Federation Gateway...")

    async with sse_client(GATEWAY_URL) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(f"\nConnected! {len(tools.tools)} tools available:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Discover merchants
            print("\n--- Discovering merchants ---")
            result = await session.call_tool("federation_list_tenants", {})
            tenants = json.loads(result.content[0].text)
            print(f"Found {len(tenants)} merchant(s):")
            for tenant in tenants:
                name = tenant.get("name", tenant.get("tenant_id", "Unknown"))
                print(f"  - {name}")

            # Search products on the first merchant
            if tenants:
                tenant_id = tenants[0].get("tenant_id", tenants[0].get("id"))
                print(f"\n--- Searching products on {tenants[0].get('name', tenant_id)} ---")
                result = await session.call_tool("catalog_search", {
                    "tenant_id": tenant_id,
                    "query": "shoes",
                })
                products = json.loads(result.content[0].text)
                if isinstance(products, list):
                    print(f"Found {len(products)} product(s):")
                    for product in products[:5]:
                        name = product.get("name", "Unknown")
                        price = product.get("price", "N/A")
                        print(f"  - {name} — ${price}")
                else:
                    print(json.dumps(products, indent=2))

            print("\nDone!")


if __name__ == "__main__":
    asyncio.run(main())
