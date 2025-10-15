from pydantic import BaseModel
from datetime import datetime


class Prompt(BaseModel):
    timestamp: datetime
    response: str
    prompt: str


class PromptRequest(BaseModel):
    prompt: str