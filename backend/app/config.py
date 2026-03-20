import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # LLM Configurations
    gemini=os.getenv("GOOGLE_API_KEY")
    groq=os.getenv("GROQ_API_KEY")

    # Database Configurations
    database = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    name="gemini"
