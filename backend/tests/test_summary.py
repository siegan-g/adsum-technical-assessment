from decimal import Decimal
from datetime import datetime, timezone
import pytest
from fastapi import FastAPI

from application.dependency_container import get_summary_service
from application.services.summary import SummaryService
from models.summary import Summary


class _StubSummaryService(SummaryService):
    def __init__(self):
        pass

    def get(
        self, from_date: datetime = datetime.now(), to_date: datetime = datetime.now()
    ) -> Summary:
        return Summary(
            total_payments_amount=Decimal("30.00"),
            total_payments_count=3,
            total_invoices_amount=Decimal("50.00"),
            total_invoices_count=5,
            paid_invoices_amount=Decimal("40.00"),
            paid_invoices_count=4,
            unpaid_invoices_amount=Decimal("10.00"),
            unpaid_invoices_count=1,
        )


def test_summary_route_returns_summary(app: FastAPI, client):
    app.dependency_overrides[get_summary_service] = lambda: _StubSummaryService()
    try:
        response = client.get(
            "/api/summary/",
            params={
                "from_date": datetime.now(timezone.utc).isoformat(),
                "to_date": datetime.now(timezone.utc).isoformat(),
            },
        )
        assert response.status_code == 200
        body = response.json()
        assert body["total_payments_count"] == 3
        assert body["total_invoices_count"] == 5

        assert body["total_payments_amount"] == "30.00"
        assert body["paid_invoices_amount"] == "40.00"
    finally:
        app.dependency_overrides.pop(get_summary_service, None)


def test_summary_service_aggregate_sums_and_counts():
    from models.payments import Payment
    from datetime import timezone

    # Construct minimal payment objects with Decimal amounts
    payments = [
        Payment(
            id=1,
            amount=Decimal("1.10"),
            currency="GBP",
            status="Paid",
            merchant="FNB",
            timestamp=datetime.now(timezone.utc),
        ),
        Payment(
            id=2,
            amount=Decimal("2.20"),
            currency="GBP",
            status="Pending",
            merchant="HBSC",
            timestamp=datetime.now(timezone.utc),
        ),
    ]

    svc = _StubSummaryService()
    total, count = svc.aggregate(
        payments, from_date=datetime.now(timezone.utc), to_date=datetime.now(timezone.utc)
    )
    assert str(total) == "3.30"
    assert count == 2
