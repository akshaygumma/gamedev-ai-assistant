from dotenv import load_dotenv

import os

load_dotenv()

class Settings:
    PROJECT_NAME = os.getenv("PROJECT_NAME", "GameDev AI Assistant")
    PROJECT_VERSION = os.getenv("PROJECT_VERSION", "0.1.0")
    DEBUG = os.getenv("DEBUG", "False") == "True"
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")
    LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")
    LLM_API_KEY = os.getenv("LLM_API_KEY")
    SUPABASE_URL = os.getenv("SUPABASE_URL","")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY","")

settings = Settings()