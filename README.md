# Genterr Examples

Welcome to the Genterr Examples repository!

This repository contains a collection of example projects demonstrating how to use the Genterr SDK in various scenarios. These examples are designed to help you get started quickly and inspire you with different use cases.

## Examples

### Simple Agent

This is a basic example of creating a Genterr agent that performs a simple task.

\```python
from genterr_sdk import SimpleAgent
import asyncio

async def main():
    agent = SimpleAgent(
        name="simple_agent",
        description="A simple Genterr agent"
    )
    result = await agent.process_task({"message": "Hello, Genterr!"})
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
\```

### Customer Support Agent

An example of an agent that handles customer support inquiries.

\```python
from genterr_sdk import SimpleAgent
import asyncio

async def main():
    agent = SimpleAgent(
        name="support_agent",
        description="A customer support Genterr agent"
    )
    result = await agent.process_task({"message": "How can I help you today?"})
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
\```

### Advanced Agent

An example of an advanced agent with additional features.

\```python
from genterr_sdk import AdvancedAgent
import asyncio

async def main():
    agent = AdvancedAgent(
        name="advanced_agent",
        description="An advanced Genterr agent with additional features"
    )
    result = await agent.process_task({"message": "What advanced features do you offer?"})
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
\```