from application.services.unit_of_work import UnitOfWork
from infrastructure.database.session import create_sqlmodel_engine, session_factory
from application.logging.logger import Logger
from models.summary import Summary
from models.invoices import Invoice
from models.payments import Payment
from decimal import Decimal
from datetime import datetime
from typing import List, Optional


class SummaryService:
    def __init__(self, engine, logger: Logger):
        self.engine = engine
        self.logger = logger
        
    def aggregate(self, results: List[Payment] | List[Invoice], from_date: datetime, to_date: datetime, status: Optional[str] = None):
        filters = {}
        filters['from_date'] = from_date
        filters['to_date'] = to_date
        filters['status'] = status
        
        amount = sum(result.amount for result in results)
        count = len(results)
        
        return amount, count
    
    def get(self, from_date: datetime = datetime.now(), to_date: datetime = datetime.now()) -> Summary:
        self.logger.debug(f"Getting summary from {from_date} to {to_date}")
        with UnitOfWork(session_factory=session_factory(self.engine)) as uow:
            filters = {}
            filters['from_date'] = from_date
            filters['to_date'] = to_date
            
            payments = uow.payments.read(offset=None, limit=None, **filters)
            total_payments_amount, total_payments_count = self.aggregate(payments, from_date=from_date, to_date=to_date)
            invoices = uow.invoices.read(offset=None, limit=None, **filters)
            total_invoices_amount, total_invoices_count = self.aggregate(invoices, from_date=from_date, to_date=to_date)
            
            filters['status'] = "Paid"
            
            invoices = uow.invoices.read(offset=None, limit=None, **filters)
            paid_invoices_amount, paid_invoices_count = self.aggregate(invoices, from_date=from_date, to_date=to_date)
            
            
            filters['status'] = "Unpaid"
            
            invoices = uow.invoices.read(offset=None, limit=None, **filters)
            unpaid_invoices_amount, unpaid_invoices_count = self.aggregate(invoices, from_date=from_date, to_date=to_date)
            
            uow.commit()
            
            self.logger.info(f"Successfully generated summary with {total_payments_count} payments and {total_invoices_count} invoices")
            
            # Return aggregated summary
            return Summary(
                total_payments_amount=Decimal(str(total_payments_amount)),
                total_payments_count=total_payments_count,
                total_invoices_amount=Decimal(str(total_invoices_amount)),
                total_invoices_count=total_invoices_count,
                paid_invoices_amount=Decimal(str(paid_invoices_amount)),
                paid_invoices_count=paid_invoices_count,
                unpaid_invoices_amount=Decimal(str(unpaid_invoices_amount)),
                unpaid_invoices_count=unpaid_invoices_count,
            )

