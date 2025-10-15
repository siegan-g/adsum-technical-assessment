from pydantic import BaseModel
from datetime import datetime


class PromptResponse(BaseModel):
    timestamp: datetime
    response: str | None
    prompt: str | None


class PromptRequest(BaseModel):
    prompt: str | None