from application.services.unit_of_work import UnitOfWork
from infrastructure.database.session import session_factory
from models.logs import Logs, LogsPaginate
from typing import Any, List
from sqlalchemy.engine import Engine


class AgentLogsService:
    def __init__(self, engine:Engine):
        self.engine = engine
        
    def read(self, paginate:LogsPaginate, **filters:Any)->List[Logs]:
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            logs = uow.logs.read(paginate.offset, paginate.limit, **filters)
            uow.commit()
            return logs
    
    def insert(self, log: Logs):
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            uow.logs.insert(log)
            uow.commit()
            return log
    
    def update(self, log: Logs):
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            uow.logs.update(log)
            uow.commit()
            
    def count(self,**filters: Any) -> int | None:
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            count = uow.logs.count(**filters)
            uow.commit()
            return count
