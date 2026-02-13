# Claude Desktop + ComOS Federation

Connect Claude Desktop to the ComOS Federation Gateway and shop any store on the network.

## Setup (30 seconds)

### 1. Find your config file

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### 2. Add the ComOS gateway

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

### 3. Restart Claude Desktop

The ComOS tools should now appear in Claude's tool list.

## Example Conversation

**You:** What stores are available on ComOS?

**Claude:** *Uses `federation_list_tenants`* — Let me check the available stores on the ComOS network.

I found the following stores:
- **VNM Sport** — Athletic footwear and sportswear
- *(additional merchants as they join the network)*

---

**You:** Search VNM Sport for running shoes under $150

**Claude:** *Uses `catalog_search` with tenant_id and query* — Here are the running shoes under $150:

1. **Nike Air Zoom Pegasus** — $129.99
2. **Adidas Ultraboost Light** — $139.99
3. **New Balance Fresh Foam** — $109.99
...

---

**You:** Add the Pegasus to my cart

**Claude:** *Uses `cart_add_item`* — Done! Added Nike Air Zoom Pegasus ($129.99) to your cart.

---

**You:** What's in my cart?

**Claude:** *Uses `cart_view`* — Your cart contains:
- Nike Air Zoom Pegasus — $129.99
- **Total: $129.99**

## Config File

See [claude_desktop_config.json](claude_desktop_config.json) for the ready-to-use config snippet.

## Troubleshooting

- **Tools not showing?** Make sure you restarted Claude Desktop after editing the config.
- **Connection drops?** Check your internet connection. The gateway uses SSE which requires a stable connection.
- **`npx` not found?** Install Node.js from [nodejs.org](https://nodejs.org).
