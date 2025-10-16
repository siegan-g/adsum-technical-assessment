from application.services.unit_of_work import UnitOfWork
from infrastructure.database.session import session_factory
from application.logging.logger import Logger
from typing import List, Any
from models.invoices import Invoice, InvoicePaginate
from sqlalchemy.engine import Engine


class InvoicesService:
    def __init__(self, engine:Engine, logger: Logger):
        self.engine = engine
        self.logger = logger

    def read(self,paginate:InvoicePaginate, **filters:Any)->List[Invoice]:
        self.logger.debug(
            f"Reading invoices with offset={paginate.offset}, limit={paginate.limit}, filters={filters}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            invoices = uow.invoices.read(paginate.offset, paginate.limit, **filters)
            uow.commit()
            self.logger.info(f"Returned {len(invoices)} invoices")
            return invoices

    def create(self, invoice: Invoice):
        self.logger.debug(f"Creating invoice: {invoice}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            created_invoice = uow.invoices.insert(invoice)
            uow.commit()
            self.logger.info(f"Created invoice with ID: {created_invoice.id}")
            return created_invoice
