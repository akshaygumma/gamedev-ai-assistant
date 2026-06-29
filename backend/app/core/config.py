from dotenv import load_dotenv

import os

load_dotenv()

class Settings:
    PROJECT_NAME = os.getenv("PROJECT_NAME", "GameDev AI Assistant")
    PROJECT_VERSION = os.getenv("PROJECT_VERSION", "0.1.0")
    DEBUG = os.getenv("DEBUG", "False") == "True"

settings = Settings()