from typing import Optional,TypeVar ,Generic,List, Any, Type
from abc import ABC, abstractmethod
from sqlmodel import SQLModel,Field,Session,select,and_ # type: ignore
from sqlmodel.sql.expression import SelectOfScalar
# from models.payments import Payment


class OpenTaxEntity(SQLModel):
    """
    A BaseModel for any Domain in this project.
    Any Bounded Context should implement this class
    """

    id: int = Field(None, description="Entity's Unique ID",primary_key=True)
    
T = TypeVar("T",bound=OpenTaxEntity)
class GenericRepository(Generic[T],ABC):
    
    @abstractmethod
    def read(self,**filters:dict[str,Any])->List[T]:
        raise NotImplementedError()

class GenericSqlRepository(GenericRepository[T],ABC):
    def __init__(self,session:Session,model:Type[T]) -> None:
        self.session = session
        self.model = model
        
    def _build_sqlmodel_select(self,**filters:dict[str,Any])->SelectOfScalar:

        statement = select(self.model)
        where_clauses:list[Any] = []
        for key,value in filters.items():
            where_clauses.append(getattr(self.model,key)==value)
        
        if len(where_clauses)== 1 :
            statement = statement.where(where_clauses[0])
        else:
            statement = statement.where(and_(*where_clauses))
        return statement
        
    def read(self,**filters:dict[str,Any])->List[T]:
        statement = self._build_sqlmodel_select(**filters)
        # IGNORE: It seems .all() returns a Sequence[Unknown] which causes a type error
        return self.session.exec(statement).all() # type: ignore


