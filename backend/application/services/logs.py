from application.services.unit_of_work import UnitOfWork
from sqlmodel import SQLModel
from infrastructure.database.session import create_sqlmodel_engine, session_factory
from application.logging.logger import Logger
from models.logs import Logs


class AgentLogsService:
    def __init__(self, engine):
        self.engine = engine
        
    def read(self, offset, limit, **filters):
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            logs = uow.logs.read(offset, limit, **filters)
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