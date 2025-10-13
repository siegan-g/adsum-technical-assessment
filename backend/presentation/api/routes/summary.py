from fastapi import APIRouter, Query, HTTPException
from application.services import payments
from application.services import summary
from application.settings import Settings
from typing import Optional
from datetime import datetime
from models.summary import Summary, SummaryFilter

router = APIRouter(prefix="/summary", tags=["summary"])
settings = Settings()
app_settings = settings.get_app_settings()


@router.get("/", response_model=Summary)
async def read_payments(
    from_date: datetime ,
    to_date: datetime
):
    filters = SummaryFilter(
        from_date=from_date, to_date=to_date
    )
    results = summary.get(**filters.model_dump())
    return results
