from application.services.unit_of_work import UnitOfWork
from sqlmodel import SQLModel
from infrastructure.database.session import create_sqlmodel_engine, session_factory
from application.logging.logger import Logger
from models.logs import Logs


class LogsService:
    def __init__(self, engine, logger: Logger):
        self.engine = engine
        self.logger = logger
        
    def read(self, offset, limit, **filters):
        self.logger.debug(f"Reading logs with offset={offset}, limit={limit}, filters={filters}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            logs = uow.logs.read(offset, limit, **filters)
            uow.commit()
            self.logger.info(f"Successfully retrieved {len(logs)} logs")
            return logs
    
    def insert(self, log: Logs):
        self.logger.debug(f"Inserting log: {log}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            uow.logs.insert(log)
            uow.commit()
            self.logger.info(f"Successfully inserted log with id {log.id}")
            return log
    
    def update(self, log: Logs):
        self.logger.debug(f"Updating log: {log}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            uow.logs.update(log)
            uow.commit()
            self.logger.info(f"Successfully updated log with id {log.id}")