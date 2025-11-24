from google.adk import Agent
from google.adk.models import Gemini

from capstone.config.config import retry_config

flash_card_agent = Agent(
    name="FlashCardAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""
        You are the Flashcard Agent.
        Your task is to generate educational flashcards based only on the provided text.
        
        INPUT:
        {{search_extract}}
        
        GUIDELINES:
        - Make 8–12 flashcards.
        - Each flashcard must be a question-answer pair.
        - Keep answers short (1 sentence max).
        - Avoid duplicates.
        
        OUTPUT FORMAT (JSON):
        {
          "flashcards": [
            {"question": "...", "answer": "..."},
            ...
          ]
        }
    """,
    output_key="flashcard_results",  # The result of this agent will be stored in the session state with this key.
)