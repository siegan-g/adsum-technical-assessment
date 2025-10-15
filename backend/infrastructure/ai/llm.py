from abc import ABC,abstractmethod
class Llm(ABC):
    @abstractmethod
    def generate_text(self,message:str | None)->str | None:
        raise NotImplementedError()
