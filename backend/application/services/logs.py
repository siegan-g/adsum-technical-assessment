from application.services.unit_of_work import UnitOfWork
from sqlmodel import SQLModel
from infrastructure.database.session import create_sqlmodel_engine, session_factory
from application.settings import Settings
from models.logs import Logs

settings = Settings()
db_settings = settings.get_db_settings()
engine = create_sqlmodel_engine(db_settings['url'])
SQLModel.metadata.create_all(engine)

def read(offset,limit,**filters):
    with UnitOfWork(session_factory=session_factory(engine)) as uow:
        logs = uow.logs.read(offset,limit,**filters)
        uow.commit()
        return logs 
    
def insert(log: Logs):
    with UnitOfWork(session_factory=session_factory(engine)) as uow:
        uow.logs.insert(log)
        uow.commit()
        return log
    
def update(log: Logs):
    with UnitOfWork(session_factory=session_factory(engine)) as uow:
        uow.logs.update(log)
        uow.commit()