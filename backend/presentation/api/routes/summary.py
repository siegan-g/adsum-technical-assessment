from fastapi import APIRouter, Depends
from application.services.summary import SummaryService
from application.dependency_container import get_summary_service
from datetime import datetime
from models.summary import Summary, SummaryFilter

router = APIRouter(prefix="/summary", tags=["summary"])


@router.get("/", response_model=Summary)
async def get_summary(
    from_date: datetime,
    to_date: datetime,
    summary_service: SummaryService = Depends(get_summary_service)
):
    filters = SummaryFilter(
        from_date=from_date, to_date=to_date
    )
    results = summary_service.get(**filters.model_dump())
    return results
