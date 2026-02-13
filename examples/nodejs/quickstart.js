/**
 * ComOS Federation Gateway — Node.js Quickstart
 *
 * Connects to the ComOS Federation Gateway via MCP SSE,
 * lists available merchants, and searches for products.
 */

import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { SSEClientTransport } from "@modelcontextprotocol/sdk/client/sse.js";

const GATEWAY_URL = "https://mcp.comos-gateway.com/mcp/sse";

async function main() {
  console.log("Connecting to ComOS Federation Gateway...");

  const transport = new SSEClientTransport(new URL(GATEWAY_URL));
  const client = new Client({ name: "comos-example", version: "1.0.0" });
  await client.connect(transport);

  // List available tools
  const { tools } = await client.listTools();
  console.log(`\nConnected! ${tools.length} tools available:`);
  for (const tool of tools) {
    console.log(`  - ${tool.name}: ${tool.description}`);
  }

  // Discover merchants
  console.log("\n--- Discovering merchants ---");
  const tenantsResult = await client.callTool({
    name: "federation_list_tenants",
    arguments: {},
  });
  const tenants = JSON.parse(tenantsResult.content[0].text);
  console.log(`Found ${tenants.length} merchant(s):`);
  for (const tenant of tenants) {
    console.log(`  - ${tenant.name || tenant.tenant_id || "Unknown"}`);
  }

  // Search products on the first merchant
  if (tenants.length > 0) {
    const tenantId = tenants[0].tenant_id || tenants[0].id;
    console.log(
      `\n--- Searching products on ${tenants[0].name || tenantId} ---`
    );
    const productsResult = await client.callTool({
      name: "catalog_search",
      arguments: { tenant_id: tenantId, query: "shoes" },
    });
    const products = JSON.parse(productsResult.content[0].text);
    if (Array.isArray(products)) {
      console.log(`Found ${products.length} product(s):`);
      for (const product of products.slice(0, 5)) {
        console.log(`  - ${product.name || "Unknown"} — $${product.price || "N/A"}`);
      }
    } else {
      console.log(JSON.stringify(products, null, 2));
    }
  }

  console.log("\nDone!");
  await client.close();
}

main().catch(console.error);
