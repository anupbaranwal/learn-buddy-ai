from google.adk.agents import SequentialAgent

from capstone.agents.aggregator_agent import aggregator_agent
from capstone.agents.controller_agent import controller_agent
from capstone.agents.parallel_agent import parallel_agent

root_agent = SequentialAgent(
    name="LearnBuddyAgent",
    sub_agents=[controller_agent, parallel_agent, aggregator_agent],
)