import asyncio
from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner

from capstone.agents.chat_buddy_agent import chat_buddy_agent
from capstone.agents.root_agent import root_agent

async def launch_learn_buddy():
    load_dotenv()

    print("Learn Buddy is ready!")
    print("What would you like to learn today? Tell me the topic name and start learning!.")
    print("Or just type 'exit' to end the session.\n")

    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        exit()

    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug("Photosynthesis")

if __name__ == "__main__":
    asyncio.run(launch_learn_buddy())