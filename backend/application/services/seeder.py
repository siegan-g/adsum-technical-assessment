from application.logging.logger import Logger
from application.services.payments import PaymentsService
from application.services.invoices import InvoicesService
from models.payments import Payment
from models.invoices import Invoice
from decimal import Decimal
from random import choice, randint, uniform
from datetime import datetime, timedelta, timezone

class SeederService:
    def __init__(self, engine, logger: Logger, payments_service: PaymentsService, invoices_service: InvoicesService) -> None:
        self.engine = engine
        self.logger = logger
        self.payments_service = payments_service
        self.invoices_service = invoices_service

    def _random_currency(self) -> str:
        return choice(["GBP", "ZAR"]) 

    def _random_status(self) -> str:
        return choice(["Pending", "Paid", "Fail"])

    def _random_merchant(self) -> str:
        return choice(["HSBC", "FNB", "Barclays","Standard Bank"])

    def _random_amount(self) -> Decimal:
        return Decimal(str(uniform(50,50000)))

    def _random_timestamp(self) -> datetime:
        days_ago = randint(0, 60)
        return datetime.now(timezone.utc) - timedelta(days=days_ago, hours=randint(0, 23))

    def _random_due_date(self) -> datetime:
        return datetime.now(timezone.utc) + timedelta(days=randint(0, 45))

    def seed(self, num_payments: int = 30, num_invoices: int = 30) -> None:
        self.logger.info(f"Starting database seeding: payments={num_payments}, invoices={num_invoices}")

        for _ in range(num_payments):
            payment = Payment(
                id=None,
                amount=self._random_amount(),
                currency=self._random_currency(),
                status=self._random_status(),
                merchant=self._random_merchant(),
                timestamp=self._random_timestamp(),
            )
            self.payments_service.create(payment)

        for _ in range(num_invoices):
            invoice = Invoice(
                id=None,
                amount=self._random_amount(),
                currency=self._random_currency(),
                status=self._random_status(),
                client=f"Client {randint(1, 20)}",
                due_date=self._random_due_date(),
                timestamp=self._random_timestamp(),
            )
            self.invoices_service.create(invoice)

        self.logger.info("Database seeding completed")


