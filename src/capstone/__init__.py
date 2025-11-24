import asyncio
import os


from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner

from capstone.agents.root_agent import root_agent


async def launch_learn_buddy():
    load_dotenv()

    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug("Photosynthesis")


if __name__ == "__main__":
    asyncio.run(launch_learn_buddy())