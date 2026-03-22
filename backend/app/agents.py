from langchain_classic.agents import create_agent
from.llm import llm
from langchain_core.messages import ChatPromptTemplate


prompt =ChatPromptTemplate.from_messages ('system', "You are a helpful assistant that can answer questions and perform tasks.") 


agent=create_agent(
    model=llm,
    system_prompt=prompt,
    tools=[]) 

