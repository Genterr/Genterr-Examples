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