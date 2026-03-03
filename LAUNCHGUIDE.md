# ComOS Federation Gateway

## Tagline
AI commerce control plane — one MCP connection, every merchant, full checkout.

## Description
The ComOS Federation Gateway gives AI agents complete programmatic control of a live multi-merchant commerce network through a single MCP connection. Connect once and your agent can browse catalogs, manage carts, complete checkouts with Stripe payments, track orders, handle returns, and manage inventory across every merchant on the ComOS network. 39 MCP tools including 30 dedicated commerce operations plus a pass-through to the full REST API (43 endpoints). Production-validated with 5 active tenants, OAuth 2.1 with PKCE, sub-100ms agent execution, and per-tenant circuit breakers. Built for agent developers who need real commerce capabilities — not mock data, not sandboxes, live merchants with live inventory and live payments.

## Setup Requirements
No setup required — this is a hosted remote MCP server. Connect directly to the endpoint.

## Category
Business Tools

## Features
- Search product catalogs across multiple live merchant storefronts
- Add items to cart, update quantities, and manage shopping sessions
- Complete full checkout flow including shipping selection and Stripe payment
- View order history and track shipments
- Discover all available merchants dynamically at runtime
- Guest sessions for browsing and cart operations without authentication
- OAuth 2.1 with PKCE for authenticated operations (orders, returns, agent management)
- Per-tenant circuit breakers for fault isolation
- Stateless JWT design — horizontally scalable, no sticky sessions
- Full REST API pass-through via api_call tool (43 endpoints, 100% platform coverage)
- Check inventory and stock availability
- Manage returns and support tickets
- Get personalized product recommendations
- Enterprise SSO compatible (Okta, Azure AD, any OIDC provider)

## Getting Started
- "What stores are available?" — discovers all live merchants on the network
- "Search for running shoes on vnm-sport" — searches a specific merchant's catalog
- "Add that to my cart and start checkout" — full cart-to-payment flow
- "Show me my recent orders" — order history (requires authentication)
- Tool: federation_list_tenants — Discover all available merchant storefronts
- Tool: catalog_search — Search products by keyword on any merchant
- Tool: cart_add_item — Add a product to your shopping cart
- Tool: checkout_start — Begin the checkout process with shipping details
- Tool: checkout_create_payment_session — Get a live Stripe payment link
- Tool: orders_list — View order history for a merchant

## Tags
commerce, ecommerce, shopping, ai-commerce, mcp, federation, multi-tenant, checkout, stripe, payments, catalog, cart, orders, inventory, oauth, enterprise, saas, marketplace, merchant-network, agent-commerce, agentic-commerce, retail, product-search, order-tracking, returns

## Documentation URL
https://comos-portal.com

## Health Check URL
https://mcp.comos-gateway.com/health
