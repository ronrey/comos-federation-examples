# Node.js + ComOS Federation

Connect to the ComOS Federation Gateway using the MCP TypeScript SDK.

## Setup

```bash
npm install
```

## Run

```bash
node quickstart.js
```

This will:
1. Connect to the ComOS Federation Gateway via SSE
2. List available tools
3. List all merchants on the network
4. Search for products on the first available merchant
5. Display the results

## What's happening

The script uses the official `@modelcontextprotocol/sdk` package to establish an SSE connection to `https://mcp.comos-gateway.com/mcp/sse`. From there it can call any of the 25 gateway tools.

## Extend it

Use this as a foundation to build:
- Express/Fastify middleware that adds commerce to your API
- A shopping bot for Discord, Slack, or Telegram
- An automated price monitoring service
- A product recommendation engine
