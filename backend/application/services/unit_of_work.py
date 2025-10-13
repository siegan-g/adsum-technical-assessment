from models.payments import PaymentRepository
from typing import Callable
from sqlmodel import Session

class UnitOfWork:
    def __init__(self,session_factory:Callable[[],Session])->None:
        self.session_factory = session_factory
        
    def __enter__(self):
        self.session = self.session_factory()
        self.payments = PaymentRepository(self.session)
        return self
    
    def __exit__(self,exc_type,exc_value,traceback):
        self.rollback()
        
    
    def commit(self):
        self.session.commit()
        
    def rollback(self):
        self.session.rollback()