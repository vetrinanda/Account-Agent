from langchain_classic.agents import create_agent
from.llm import llm

agent=create_agent(
    model=llm,
    system_prompt="You are a helpful assistant that can answer questions and perform tasks.",
    tools=[])