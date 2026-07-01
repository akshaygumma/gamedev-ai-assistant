from groq import Groq

from app.core.config import settings
from app.schemas.llm_request import LLMRequest
from app.schemas.llm_response import LLMResponse
from app.llm.base_provider import BaseLLMProvider

class GroqProvider(BaseLLMProvider):
    def __init__(self):
        self.client = Groq(api_key=settings.LLM_API_KEY)

    def generate_response(self, request: LLMRequest) -> LLMResponse:
        response = self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=[
                {"role": "system", "content": request.system_prompt},
                {"role": "user", "content": request.user_prompt},
            ],
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        return LLMResponse(
            content=response.choices[0].message.content,
            provider="groq",
            model=settings.LLM_MODEL
        )