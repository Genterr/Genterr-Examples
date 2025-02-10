from genterr_sdk import AdvancedAgent
import asyncio

async def main():
    agent = AdvancedAgent(
        name="advanced_agent",
        description="An advanced Genterr agent with additional features"
    )
    result = await agent.process_task({"message": "What advanced features do you offer?"})
    return result  # Rückgabe des Ergebnisses

if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)