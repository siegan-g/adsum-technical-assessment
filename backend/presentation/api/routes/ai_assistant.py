from fastapi import APIRouter, Query, Depends
from typing import Optional
from application.settings import Settings
from application.services.llm  import LlmService
from application.dependency_container import get_settings, get_llm_service
from models.prompt import PromptResponse, PromptRequest

router = APIRouter(prefix="/ai-assistant", tags=["ai-assistant"])

@router.post("/", response_model=PromptResponse)
async def create_prompt(
    llm_service: LlmService = Depends(get_llm_service),
    body: PromptRequest | None = None,
):
    message = body.prompt if body else ""
    result = llm_service.create_text(message)
    return result 
