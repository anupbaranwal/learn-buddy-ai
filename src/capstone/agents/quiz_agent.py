from google.adk import Agent
from google.adk.models import Gemini

from capstone.config.config import retry_config

quiz_agent = Agent(
    name="QuizAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""
        You are the Quiz Agent.
        Your task is to create practice questions based only on the provided text.
        
        INPUT:
        {{search_extract}}
        
        GUIDELINES:
        - Create 5 multiple-choice questions (MCQ).
        - Create 5 short-answer questions.
        - Each MCQ must contain options a, b, c and one correct answer.
        - Ensure all answers are derivable from the text.
        
        OUTPUT FORMAT (JSON):
        {
          "mcq": [
            {"question": "...", "options": ["a) ...","b) ...","c) ..."], "answer": "b"}
          ],
          "short_answers": [
            {"question": "...", "answer": "..."}
          ]
        }
    """,
    output_key="quiz_results",  # The result of this agent will be stored in the session state with this key.
)


