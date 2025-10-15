from application.logging.logger import Logger
from infrastructure.ai.llm import Llm
from datetime import datetime, timezone
from models.prompt import PromptResponse

class LlmService:
    def __init__(self,logger:Logger,llm:Llm):
        self.logger =logger
        self.llm = llm

    def generate(self, message: str) -> PromptResponse:
        self.logger.info(f"Receieved Prompt: {message}")
        response_text = self.llm.generate_text(message)
        prompt_response = PromptResponse(
            timestamp=datetime.now(timezone.utc),
            response=response_text,
            prompt=message,
        )
        self.logger.info(f"Generated Response: {response_text}")
        return prompt_response
        

    