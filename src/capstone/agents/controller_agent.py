from google.adk import Agent
from google.adk.models import Gemini
from google.adk.tools import google_search

from capstone.config.config import retry_config

controller_agent = Agent(
    name="ControllerAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""
        You are the Controller Agent for an Academic Study Group system called learn buddy.
        Your job is to:
        1. Receive a student query.
        2. Create an optimized Google Search query based on the student's topic.
        3. Extract the most relevant text from search results (summary-level).
        
        DO NOT generate summaries, flashcards, quizzes yourself.
        These are created only by worker agents.
        
        Your output must always be in JSON:
        {
          "search_query": "...",
          "search_extract": "...",
          "status": "READY_FOR_WORKERS"
        }

    """,
    tools=[google_search],
    output_key="search_extract",
)