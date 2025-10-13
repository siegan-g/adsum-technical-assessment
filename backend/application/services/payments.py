from application.services.unit_of_work import UnitOfWork
from sqlmodel import SQLModel
from sqlmodel.pool import StaticPool
from infrastructure.database.session import create_sqlmodel_engine, session_factory
from models.payments import Payment
from application.settings import Settings


settings = Settings()
db_settings = settings.get_db_settings()
engine = create_sqlmodel_engine(db_settings['url'])

def read(**filters):
    with UnitOfWork(session_factory=session_factory(engine)) as uow:
        results =  uow.payments.read(**filters)
        return results
    
    