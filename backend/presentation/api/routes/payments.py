from fastapi import APIRouter, Query, HTTPException, Depends
from application.services.payments import PaymentsService
from application.dependency_container import get_payments_service, get_settings
from application.settings import Settings
from typing import Optional
from datetime import datetime
from models.payments import PaymentFilter, PaymentResponse, PaymentPaginate

router = APIRouter(prefix="/payments", tags=["payments"])

@router.get("/", response_model=PaymentResponse)
async def read_payments(
    from_date: Optional[datetime] = Query(
        None, description="Filter payments from this date"
    ),
    to_date: Optional[datetime] = Query(
        None, description="Filter payments to this date"
    ),
    status: Optional[str] = Query(None, description="Filter by payment status"),
    offset: Optional[int] = Query(None, description="Pagination offset"),
    limit: Optional[int] = Query(10, description="Pagination limit"),
    payments_service: PaymentsService = Depends(get_payments_service),
    settings: Settings = Depends(get_settings)
):
    app_settings = settings.get_app_settings()
    if limit > app_settings['max_limit']:
        raise HTTPException(status_code=400, detail=f"Query limit has been exceeded")
    filters = PaymentFilter(from_date=from_date, to_date=to_date, status=status)
    paginate = PaymentPaginate(offset=offset,limit=limit)
    results = payments_service.read(paginate,**filters.model_dump())
    count = payments_service.count(**filters.model_dump())
    return PaymentResponse(payments=results, payment_filter=filters,payment_paginate=paginate,count=count)
