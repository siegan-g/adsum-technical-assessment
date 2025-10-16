from application.services.unit_of_work import UnitOfWork
from infrastructure.database.session import session_factory
from application.logging.logger import Logger
from models.payments import Payment, PaymentPaginate
from typing import List, Any
from sqlalchemy.engine import Engine


class PaymentsService:
    def __init__(self, engine: Engine, logger: Logger):
        self.engine = engine
        self.logger = logger

    def read(self, paginate:PaymentPaginate, **filters: Any) -> List[Payment]:
        self.logger.debug(
            f"Reading payments with offset={paginate.offset}, limit={paginate.limit}, filters={filters}"
        )
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            payments = uow.payments.read(paginate.offset, paginate.limit, **filters)
            uow.commit()
            self.logger.info(f"Returned {len(payments)} payments")
            return payments

    def create(self, payment: Payment):
        self.logger.debug(f"Creating payment: {payment}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            created_payment = uow.payments.insert(payment)
            uow.commit()
            self.logger.info(f"Created payment with ID: {created_payment.id}")
            return created_payment

    def count(self,**filters: Any) -> int | None:
        self.logger.debug(f"Counting payments with filters={filters}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            count = uow.payments.count(**filters)
            uow.commit()
            self.logger.info(f"Found {count} payments matching filters")
            return count
