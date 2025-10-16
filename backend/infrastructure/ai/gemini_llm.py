from infrastructure.ai.llm import Llm
from google import genai
from google.genai.types import GenerateContentConfig

class GeminiLlm(Llm):
    def __init__(self,instructions:str,api_key:str)->None: 
        self.client = genai.Client(api_key=api_key)
        self.instructions = instructions
        
    def generate_text(self, message: str) -> str | None:
        response = self.client.models.generate_content(model="gemini-2.5-flash",contents=message,config=GenerateContentConfig(system_instruction=self.instructions)) # type: ignore
        return response.text