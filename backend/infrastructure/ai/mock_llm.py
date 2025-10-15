from infrastructure.ai.llm import Llm
class MockLLM(Llm):
    def __init__(self) -> None:
        super().__init__()

    def generate_text(self, message: str) -> str:
        return f"Mock response to: {message}"