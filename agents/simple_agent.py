from genterr_sdk import SimpleAgent
import asyncio

async def main():
    agent = SimpleAgent(
        name="simple_agent",
        description="A simple Genterr agent"
    )
    result = await agent.process_task({"message": "Hello, Genterr!"})
    return result  # Rückgabe des Ergebnisses

if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)