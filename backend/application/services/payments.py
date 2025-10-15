from application.services.unit_of_work import UnitOfWork
from infrastructure.database.session import session_factory
from application.logging.logger import Logger
from models.payments import Payment

class PaymentsService:
    def __init__(self, engine, logger: Logger):
        self.engine = engine
        self.logger = logger
        
    def read(self, offset, limit, **filters):
        self.logger.debug(f"Reading payments with offset={offset}, limit={limit}, filters={filters}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            payments = uow.payments.read(offset, limit, **filters)
            uow.commit()
            self.logger.info(f"Returned {len(payments)} payments")
            return payments

    def create(self,payment:Payment):
        self.logger.debug(f"Creating payment: {payment}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            created_payment = uow.payments.insert(payment)
            uow.commit()
            self.logger.info(f"Created payment with ID: {created_payment.id}")
            return created_payment
    