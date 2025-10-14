from fastapi import APIRouter
from routes import health,payments,invoices,summary, logs


api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(payments.router)
api_router.include_router(invoices.router)
api_router.include_router(summary.router)
api_router.include_router(logs.router)