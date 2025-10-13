from fastapi import APIRouter, Query
from application.services import payments
from typing import Optional
from datetime import datetime
from models.payments import PaymentFilter
router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("/")
async def read_payments(from_date:Optional[datetime] = Query(None,description="Filter payments from this date"),
                        to_date:Optional[datetime]=Query(None,description="Filter payments to this date"),
                        status:Optional[str]=Query(None,description="Filter by payment status")):
    filters = PaymentFilter(from_date=from_date,to_date=to_date,status=status)
    return payments.read(**filters.model_dump())