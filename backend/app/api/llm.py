from fastapi import APIRouter

from app.schemas.llm_request import LLMRequest
from app.llm.provider_factory import LLMProviderFactory

router = APIRouter()

@router.post("/llm/test")
async def test_llm():
    provider = LLMProviderFactory.get_provider()
    response = provider.generate_response(LLMRequest(
        system_prompt="You are a helpful assistant.",
        user_prompt="What is the capital of France?",
    ))
    return response