from decimal import Decimal
from datetime import datetime, timezone
import pytest
from fastapi import FastAPI

from application.dependency_container import get_invoices_service, get_settings
from application.services.invoices import InvoicesService
from application.settings import Settings
from models.invoices import Invoice


class _StubInvoicesService(InvoicesService):
    def __init__(self):  
        pass

    def read(self, offset, limit, **filters): 
        return [
            Invoice(
                id=1,
                amount=Decimal("10.00"),
                currency="GBP",
                status="Paid",
                due_date=datetime.now(timezone.utc),
                client="A",
                timestamp=datetime.now(timezone.utc),
            ),
            Invoice(
                id=2,
                amount=Decimal("20.00"),
                currency="GBP",
                status="Pending",
                due_date=datetime.now(timezone.utc),
                client="B",
                timestamp=datetime.now(timezone.utc),
            ),
        ]


@pytest.mark.anyio
async def test_invoices_limit_exceeds_returns_400(client):
    settings: Settings = get_settings()
    max_limit = settings.get_app_settings()["max_limit"]

    response = await client.get(f"/api/invoices/?limit={max_limit + 1}")
    assert response.status_code == 400


@pytest.mark.anyio
async def test_invoices_returns_list_when_ok(app: FastAPI, client):
    app.dependency_overrides[get_invoices_service] = lambda: _StubInvoicesService()
    try:
        response = await client.get("/api/invoices/?limit=2")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        assert {item["client"] for item in data} == {"A", "B"}
    finally:
        app.dependency_overrides.pop(get_invoices_service, None)

