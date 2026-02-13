# Python + ComOS Federation

Connect to the ComOS Federation Gateway using the MCP Python SDK.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python quickstart.py
```

This will:
1. Connect to the ComOS Federation Gateway via SSE
2. List available tools
3. List all merchants on the network
4. Search for products on the first available merchant
5. Display the results

## What's happening

The script uses the official `mcp` Python package to establish an SSE connection to `https://mcp.comos-gateway.com/mcp/sse`. From there it can call any of the 25 gateway tools — discovery, catalog search, cart management, checkout, and order tracking.

## Extend it

The `quickstart.py` is a starting point. You can extend it to:
- Build a CLI shopping tool
- Integrate with your own agent framework
- Create automated purchasing workflows
- Monitor product availability across stores
