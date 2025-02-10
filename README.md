# Genterr Examples

Welcome to the Genterr Examples repository!

This repository contains a collection of example projects demonstrating how to use the Genterr SDK in various scenarios. These examples are designed to help you get started quickly and inspire you with different use cases.

## Table of Contents

- [Introduction](#introduction)
- [Examples](#examples)
  - [Simple Agent](#simple-agent)
  - [Customer Support Agent](#customer-support-agent)
- [License](#license)

## Introduction

The Genterr SDK enables developers to create powerful AI agents that can be operated on the Genterr platform. This repository provides practical examples to help you get started and demonstrate the versatile use cases of the SDK.

## Examples

### Simple Agent

This is a basic example of creating a Genterr agent that performs a simple task.

```python
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