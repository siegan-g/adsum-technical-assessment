from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime 

class Summary(BaseModel, table=False):
    total_payments_amount: Decimal 
    total_payments_count: int
    total_invoices_amount: Decimal
    total_invoices_count: int
    
    paid_invoices_amount: Decimal
    paid_invoices_count: int
    unpaid_invoices_amount: Decimal
    unpaid_invoices_count: int
    
class SummaryFilter(BaseModel):
    from_date:datetime
    to_date:datetime

