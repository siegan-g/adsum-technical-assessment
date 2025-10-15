from application.services.unit_of_work import UnitOfWork
from sqlmodel import SQLModel
from infrastructure.database.session import create_sqlmodel_engine, session_factory
from application.logging.logger import Logger


class InvoicesService:
    def __init__(self, engine, logger: Logger):
        self.engine = engine
        self.logger = logger
        
    def read(self, offset, limit, **filters):
        self.logger.debug(f"Reading invoices with offset={offset}, limit={limit}, filters={filters}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            invoices = uow.invoices.read(offset, limit, **filters)
            uow.commit()
            self.logger.info(f"Returned {len(invoices)} invoices")
            return invoices
    