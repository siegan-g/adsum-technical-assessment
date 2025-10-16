from decimal import Decimal
from datetime import datetime, timezone
import pytest
from fastapi import FastAPI

from application.dependency_container import get_invoices_service, get_settings
from application.services.invoices import InvoicesService
from application.settings import Settings
from models.invoices import Invoice, InvoiceResponse, InvoiceFilter, InvoicePaginate


class _StubInvoicesService(InvoicesService):
    def __init__(self):  
        pass

    def read(self, paginate, **filters): 
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
    
    def count(self, **filters):
        return 2


def test_invoices_limit_exceeds_returns_400(client):
    settings: Settings = get_settings()
    max_limit = settings.get_app_settings()["max_limit"]

    response = client.get(f"/api/invoices/?limit={max_limit + 1}")
    assert response.status_code == 400


def test_invoices_returns_response_when_ok(app: FastAPI, client):
    app.dependency_overrides[get_invoices_service] = lambda: _StubInvoicesService()
    try:
        response = client.get("/api/invoices/?limit=2")
        assert response.status_code == 200
        data = response.json()
        
        # Test the new response structure
        assert "invoices" in data
        assert "invoice_filter" in data
        assert "invoice_paginate" in data
        assert "count" in data
        
        # Test invoices data
        invoices = data["invoices"]
        assert isinstance(invoices, list)
        assert len(invoices) == 2
        assert {item["client"] for item in invoices} == {"A", "B"}
        
        # Test pagination data
        assert data["count"] == 2
        assert data["invoice_paginate"]["limit"] == 2
        
        # Test filter data
        assert data["invoice_filter"] is not None
    finally:
        app.dependency_overrides.pop(get_invoices_service, None)

