from application.logging.logger import Logger
from infrastructure.ai.llm import Llm
from datetime import datetime, timezone
from models.prompt import PromptResponse

class LlmService:
    def __init__(self,logger:Logger,llm:Llm):
        self.logger =logger
        self.llm = llm

    def create_text(self, message: str | None) -> PromptResponse:
        response_text = self.llm.generate_text(message)
        prompt_response = PromptResponse(
            timestamp=datetime.now(timezone.utc),
            response=response_text,
            prompt=message,
        )
        return prompt_response
        

    