from google.adk import Agent
from google.adk.models import Gemini

from capstone.config.config import retry_config

aggregator_agent = Agent(
    name="AggregatorAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    # It uses placeholders to inject the outputs from the parallel agents, which are now in the session state.
    instruction="""
        You are the Output Combiner Agent.
        Your job is to merge responses from all worker agents into one structured final response.
        
        INPUT:
        - Summary Agent output {final_summary}
        - Flashcard Agent output {flashcard_results}
        - Quiz Agent output {quiz_results}
        
        GUIDELINES:
        - Do not modify the content from workers.
        - Organize neatly under headings: Summary, Flashcards, Quiz
        
        OUTPUT FORMAT:
        {
          "summary": "...",
          "flashcards": [...],
          "quiz": {
            "mcq": [...],
            "short_answers": [...]
          }
        }
    """,
    output_key="executive_summary",  # This will be the final output of the entire system.
)