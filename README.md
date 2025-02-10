# Genterr-Examples

This repository contains example agents, tests, and documentation for Genterr.

## Installation

Ensure you have Python 3.8 or higher installed.

1. Clone the repository:
    ```bash
    git clone https://github.com/Genterr/Genterr-Examples.git
    cd Genterr-Examples
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install the `genterr-sdk`:
    ```bash
    pip install https://github.com/Genterr/genterr-sdk
    ```

## Example Agents

### Customer Support Agent

This agent provides support for customer inquiries.

```python name=agents/customer_support_agent.py
from genterr_sdk import SimpleAgent
import asyncio

async def main():
    agent = SimpleAgent(
        name="support_agent",
        description="A customer support Genterr agent"
    )
    result = await agent.process_task({"message": "How can I help you today?"})
    return result

if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)
