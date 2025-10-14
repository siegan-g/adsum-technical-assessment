from fastapi import APIRouter, Query, HTTPException
from application.services import logs 
from application.settings import Settings
from typing import Optional
from datetime import datetime
from models.logs import Logs, LogsFilter

router = APIRouter(prefix="/agent-logs", tags=["logs"])
settings = Settings()
app_settings = settings.get_app_settings()

@router.get("/", response_model=list[Logs])
async def read_payments(
    from_date: Optional[datetime] = Query(
        None, description="Filter logs from this date"
    ),
    to_date: Optional[datetime] = Query(
        None, description="Filter logs to this date"
    ),
    level: Optional[str] = Query(None, description="Filter by log status"),
    offset: Optional[int] = Query(None, description="Pagination offset"),
    limit: Optional[int] = Query(10, description="Pagination limit"),
):
    if limit > app_settings['max_limit']:
        raise HTTPException(status_code=400, detail=f"Query limit has been exceeded")
    filters = LogsFilter(from_date=from_date, to_date=to_date, level=level,offset=offset,limit=limit)
    results = logs.read(**filters.model_dump())
    return results 