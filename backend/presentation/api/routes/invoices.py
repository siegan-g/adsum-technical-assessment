from fastapi import APIRouter, Query, HTTPException
from application.services import invoices 
from application.settings import Settings
from typing import Optional
from datetime import datetime
from models.invoices import InvoiceFilter,Invoice 

router = APIRouter(prefix="/invoices", tags=["invoices"])
settings = Settings()
app_settings = settings.get_app_settings()

@router.get("/", response_model=list[Invoice])
async def read_payments(
    from_date: Optional[datetime] = Query(
        None, description="Filter invoices from this date"
    ),
    to_date: Optional[datetime] = Query(
        None, description="Filter invoices to this date"
    ),
    status: Optional[str] = Query(None, description="Filter by payment status"),
    offset: Optional[int] = Query(None, description="Pagination offset"),
    limit: Optional[int] = Query(10, description="Pagination limit"),
):
    if limit > app_settings['max_limit']:
        raise HTTPException(status_code=400, detail=f"Query limit has been exceeded")
    filters = InvoiceFilter(from_date=from_date, to_date=to_date, status=status,offset=offset,limit=limit)
    results = invoices.read(**filters.model_dump())
    return results 
