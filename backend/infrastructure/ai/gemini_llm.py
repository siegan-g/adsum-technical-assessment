from infrastructure.ai.llm import Llm
from google import genai
from typing import Any  

class GeminiLlm(Llm):
    def __init__(self,api_key:str)->None: 
        self.client = genai.Client(api_key=api_key)
        
    def generate_text(self, message: str) -> str | None:
        response = self.client.models.generate_content(model="gemini-2.5-flash",contents=message)
        return response.text