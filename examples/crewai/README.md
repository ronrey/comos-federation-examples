# CrewAI + ComOS Federation

A multi-agent shopping crew where specialized agents collaborate to find and purchase products through the ComOS Federation Gateway.

## Setup

```bash
pip install -r requirements.txt
```

Set your OpenAI API key:

```bash
export OPENAI_API_KEY=your-key-here
```

## Run

```bash
python shopping_crew.py
```

## The Crew

| Agent | Role | What it does |
|-------|------|-------------|
| **Store Scout** | Product Researcher | Discovers merchants and searches for products matching the request |
| **Cart Manager** | Shopping Assistant | Adds selected items to the cart and manages quantities |
| **Checkout Agent** | Purchase Coordinator | Reviews the cart and initiates checkout |

## How it works

Each agent has access to specific ComOS MCP tools relevant to their role. The crew works through a sequential process:

1. **Store Scout** discovers stores and searches for matching products
2. **Cart Manager** selects the best options and adds them to the cart
3. **Checkout Agent** reviews and finalizes the purchase

## Customize

Change the `SHOPPING_REQUEST` in `shopping_crew.py` to try different scenarios:
- "Find the best wireless headphones under $200"
- "Compare athletic shoes across all stores and pick the best value"
- "Stock up on workout gear — shoes, shorts, and a water bottle"
