from fastapi import APIRouter, Query, HTTPException, Depends
from application.services.logs import AgentLogsService
from application.dependency_container import get_agent_logs_service, get_settings
from application.settings import Settings
from typing import Optional
from datetime import datetime
from models.logs import LogsFilter, LogsResponse, LogsPaginate

router = APIRouter(prefix="/agent-logs", tags=["logs"])

@router.get("/", response_model=LogsResponse)
async def read_logs(
    from_date: Optional[datetime] = Query(
        None, description="Filter logs from this date"
    ),
    to_date: Optional[datetime] = Query(
        None, description="Filter logs to this date"
    ),
    level: Optional[str] = Query(None, description="Filter by log status"),
    offset: Optional[int] = Query(None, description="Pagination offset"),
    limit: Optional[int] = Query(10, description="Pagination limit"),
    logs_service: AgentLogsService = Depends(get_agent_logs_service),
    settings: Settings = Depends(get_settings)
):
    app_settings = settings.get_app_settings()
    if limit > app_settings['max_limit']:
        raise HTTPException(status_code=400, detail=f"Query limit has been exceeded")
    filters = LogsFilter(from_date=from_date, to_date=to_date, level=level)
    paginate = LogsPaginate(offset=offset, limit=limit)
    results = logs_service.read(paginate, **filters.model_dump())
    count = logs_service.count(**filters.model_dump())
    return LogsResponse(logs=results, logs_filter=filters, logs_paginate=paginate, count=count) 