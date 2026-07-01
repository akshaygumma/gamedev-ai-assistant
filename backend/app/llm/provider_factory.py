from app.core.config import settings
from app.llm.groq_provider import GroqProvider

class LLMProviderFactory:
    @staticmethod
    def get_provider():
        if settings.LLM_PROVIDER == "groq":
            return GroqProvider()
        else:
            raise ValueError(f"Unsupported LLM provider: {settings.LLM_PROVIDER}")