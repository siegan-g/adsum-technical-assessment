from fastapi import APIRouter
from application.services import payments

router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("/")
async def read_payments(from_date:str,to_date:str):
    return payments.read(from_date=from_date,to_date=to_date)