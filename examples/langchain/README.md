# LangChain + ComOS Federation

Build a shopping agent powered by LangChain that uses ComOS MCP tools to browse stores, search products, and manage a cart.

## Setup

```bash
pip install -r requirements.txt
```

Set your OpenAI API key (or use any LangChain-supported LLM):

```bash
export OPENAI_API_KEY=your-key-here
```

## Run

```bash
python shopping_agent.py
```

The agent will:
1. Connect to the ComOS Federation Gateway
2. Discover available merchants
3. Search for products matching your query
4. Add items to a cart
5. Show the cart summary

## How it works

The script loads all 25 ComOS MCP tools as LangChain tools using the MCP-to-LangChain adapter. The LLM agent then reasons over the tools to complete shopping tasks — just like a human would browse, search, compare, and buy.

## Customize

Change the `SHOPPING_TASK` variable in `shopping_agent.py` to try different scenarios:
- "Find the cheapest wireless headphones across all stores"
- "Compare running shoes under $150"
- "Add 2 pairs of socks and a hat to my cart"
