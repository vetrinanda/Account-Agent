from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from .config import Config

if Config.name == "gemini":
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro", 
        temperature=0.7, 
        max_tokens=2048, 
        api_key=Config.gemini)
else:
    llm = ChatGroq(
        model="groq-1.5-pro", 
        temperature=0.7, 
        max_tokens=2048, 
        api_key=Config.groq)