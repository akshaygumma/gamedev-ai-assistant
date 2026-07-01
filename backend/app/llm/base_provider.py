from abc import ABC, abstractmethod

from app.schemas.llm_request import LLMRequest
from app.schemas.llm_response import LLMResponse

class BaseLLMProvider(ABC):
    @abstractmethod
    def generate_response(self, request: LLMRequest) -> LLMResponse:
        pass