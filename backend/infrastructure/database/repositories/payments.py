from infrastructure.database.repositories.base import GenericSqlRepository
from models.payments import Payment
from typing import Optional
from sqlmodel import select

class PaymentRepository(GenericSqlRepository[Payment]):
    def __init__(self, session):
        super().__init__(session, Payment)
        
    def get_paid(self,offset:Optional[int],limit:Optional[int])->list[Payment]:
        statement = select(Payment).where(Payment.status == "paid")
        if offset is not None:
            statement = statement.offset(offset)
        if limit is not None:
            statement = statement.limit(limit)
        # IGNORE: It seems .all() returns a Sequence[Unknown] which causes a type error
        return self.session.exec(statement).all() # type: ignore