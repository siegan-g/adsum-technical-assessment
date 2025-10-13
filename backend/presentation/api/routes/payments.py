from fastapi import APIRouter, Query
from application.services import payments
from typing import Optional
from datetime import datetime
from models.payments import PaymentFilter, Payment

router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("/", response_model=list[Payment])
async def read_payments(
    from_date: Optional[datetime] = Query(
        None, description="Filter payments from this date"
    ),
    to_date: Optional[datetime] = Query(
        None, description="Filter payments to this date"
    ),
    status: Optional[str] = Query(None, description="Filter by payment status"),
):
    filters = PaymentFilter(from_date=from_date, to_date=to_date, status=status)
    results = payments.read(**filters.model_dump())
    return results 
