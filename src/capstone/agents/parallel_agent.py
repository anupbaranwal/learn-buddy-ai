from google.adk.agents import ParallelAgent

from capstone.agents.flash_card_agent import flash_card_agent
from capstone.agents.quiz_agent import quiz_agent
from capstone.agents.summary_agent import summary_agent

parallel_agent = ParallelAgent(
    name="ParallelAgentTeam",
    sub_agents=[summary_agent, flash_card_agent, quiz_agent],
)