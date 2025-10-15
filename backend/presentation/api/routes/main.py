from fastapi import APIRouter
from presentation.api.routes import health, payments, invoices, summary, agent_logs, ai_assistant


api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(payments.router)
api_router.include_router(invoices.router)
api_router.include_router(summary.router)
api_router.include_router(agent_logs.router)
api_router.include_router(ai_assistant.router)
