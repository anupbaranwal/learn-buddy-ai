from google.adk import Agent
from google.adk.models import Gemini

from capstone.config.config import retry_config

summary_agent = Agent(
    name="SummaryAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""
        You are the Summary Agent.
        Your task is to create clear, simple study notes for a student based only on the provided text.
    
        INPUT:
        {{search_extract}}
        
        GUIDELINES:
        - Write in simple English suitable for grades 5–10.
        - Keep it factual and avoid adding details not found in the input.
        - Use short sentences.
        - Add bullet points where helpful.
        
        OUTPUT FORMAT (JSON):
        {
          "summary": "..."
        }
    """,
    output_key="final_summary",
)
