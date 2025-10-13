from typing import Optional,TypeVar ,Generic,List, Any
from abc import ABC, abstractmethod
from pydantic import Field, BaseModel


class OpenTaxEntity(BaseModel):
    """
    A BaseModel for any Domain in this project.
    Any Bounded Context should implement this class
    """

    id: Optional[str | int] = Field(None, description="Entity's Unique ID")

T = TypeVar("T",bound=OpenTaxEntity)
class GenericRepository(Generic[T],ABC):
    
    @abstractmethod
    def read(self,**filters:dict[str,Any])->List[T]:
        raise NotImplementedError
