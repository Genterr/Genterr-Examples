from genterr_sdk import SimpleAgent
import asyncio

async def main():
    agent = SimpleAgent(
        name="support_agent",
        description="A customer support Genterr agent"
    )
    result = await agent.process_task({"message": "How can I help you today?"})
    return result  # Rückgabe des Ergebnisses

if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)