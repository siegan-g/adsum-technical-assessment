from application.logging.logger import Logger
from infrastructure.ai.llm import Llm
from datetime import datetime
from models.prompt import Prompt

class LlmService:
    def __init__(self,logger:Logger,llm:Llm):
        self.logger =logger
        self.llm = llm

    def create_text(self, message: str) -> Prompt:
        response_text = self.llm.generate_text(message)
        prompt = Prompt(
            timestamp=datetime.utcnow(),
            response=response_text,
            prompt=message,
        )
        return prompt
        

    