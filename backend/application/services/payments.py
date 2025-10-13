from application.services.unit_of_work import UnitOfWork
from sqlmodel import SQLModel
from infrastructure.database.session import create_sqlmodel_engine, session_factory
from application.settings import Settings


settings = Settings()
db_settings = settings.get_db_settings()
engine = create_sqlmodel_engine(db_settings['url'])
SQLModel.metadata.create_all(engine)

def read(**filters):
    with UnitOfWork(session_factory=session_factory(engine)) as uow:
        payments = uow.payments.read(**filters)
        uow.commit()
        return payments
    
    