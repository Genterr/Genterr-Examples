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