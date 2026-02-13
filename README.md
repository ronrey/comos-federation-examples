# ComOS Federation Gateway — Examples

**Connect your AI agents to commerce. One connection, every store.**

The [ComOS Federation Gateway](https://comos-portal.com/gateway) is a multi-tenant MCP server that lets AI agents shop across every merchant on the ComOS network through a single connection.

## Quick Start (30 seconds)

Add this to your Claude Desktop `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "comos-gateway": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.comos-gateway.com/mcp/sse"]
    }
  }
}
```

Restart Claude Desktop. Ask Claude: *"What stores are available on ComOS?"*

That's it. You're connected.

## What You Get

**25 gateway tools** across 6 categories:

| Category | Tools | What they do |
|----------|-------|--------------|
| **Discovery** | `federation_list_tenants`, `federation_tenant_info`, `federation_help` | Find stores and get details |
| **Catalog** | `catalog_search`, `catalog_get_products`, `catalog_get_featured` | Browse and search products |
| **Cart** | `cart_view`, `cart_add_item`, `cart_update_quantity`, `cart_remove_item`, `cart_clear` | Manage shopping cart |
| **Checkout** | `checkout_start`, `checkout_status`, `checkout_list`, `checkout_shipping_options` | Complete purchases |
| **Orders** | `orders_list`, `orders_get`, `orders_track`, `orders_recent` | Track orders and shipments |
| **Agents** | `federation_list_agents`, `federation_agent_status`, `federation_list_agent_types`, `federation_get_agent_runs`, `federation_run_agent` | Manage autonomous agents |

## Examples

| Example | Description | Difficulty |
|---------|-------------|------------|
| [Claude Desktop](examples/claude-desktop/) | Connect Claude Desktop to ComOS in 30 seconds | Beginner |
| [Python](examples/python/) | Connect to the SSE endpoint, search products, manage cart | Beginner |
| [Node.js](examples/nodejs/) | Same as Python, but in JavaScript | Beginner |
| [LangChain](examples/langchain/) | Build a shopping agent with LangChain + ComOS | Intermediate |
| [CrewAI](examples/crewai/) | Multi-agent shopping crew with specialized roles | Intermediate |

## Connection Details

| | |
|---|---|
| **Endpoint** | `https://mcp.comos-gateway.com/mcp/sse` |
| **Transport** | SSE (Server-Sent Events) |
| **Auth** | Guest sessions for browsing; JWT for full access |
| **Protocol** | [MCP (Model Context Protocol)](https://modelcontextprotocol.io) |

## How It Works

```
Your AI Agent (Claude, ChatGPT, custom)
    │
    │  Single MCP connection
    ▼
ComOS Federation Gateway
    │
    │  Transparent routing via tenant_id
    ▼
┌─────────┬─────────┬─────────┐
│ Store A │ Store B │ Store C │  ← Every merchant on ComOS
└─────────┴─────────┴─────────┘
```

1. Connect once to the gateway
2. Discover merchants with `federation_list_tenants`
3. Browse products with `catalog_search`
4. Add to cart, checkout, track orders
5. Switch between stores seamlessly — no reconnection needed

## Links

- [ComOS Portal](https://comos-portal.com) — The platform
- [Gateway Page](https://comos-portal.com/gateway) — Gateway documentation
- [Demo Store](https://vnm-sport.comos-retail.com/) — Live merchant storefront
- [Smithery Listing](https://smithery.ai) — MCP registry listing
- [MCP Registry](https://registry.modelcontextprotocol.io) — Official registry listing

## License

MIT — see [LICENSE](LICENSE)
