from sqlmodel import Field
from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
from datetime import datetime, timezone
from infrastructure.database.repository import OpenTaxEntity, GenericSqlRepository

class Payment(OpenTaxEntity, table=True):
    # IGNORE: Unfortunatetly pylance/pyright doesn't play nicely with __tablename__ definitions without a hacky workaround
    # https://github.com/fastapi/sqlmodel/issues/98
    __tablename__: str = "payments"  # type: ignore
    amount: Decimal = Field(default=0, max_digits=10, decimal_places=2, nullable=False)
    currency: str = Field(default="GBP", max_length=3, nullable=False)
    status: str = Field(default="pending", max_length=20, nullable=False)
    merchant: str = Field(default="", max_length=100, nullable=False)
    timestamp: datetime = Field(default=datetime.now(timezone.utc), nullable=False)

class PaymentFilter(BaseModel):
    # Ensure BaseModel is implemented to keep a seperation of means of concern. This model should exist only on the application layer
    """
    Class with relevant filters for the Payment Class. 
    """
    from_date:Optional[datetime] = None
    to_date:Optional[datetime] = None
    status:Optional[str] = None
    offset:Optional[int] = None
    limit:Optional[int] = None

class PaymentRepository(GenericSqlRepository[Payment]):
    def __init__(self, session):
        super().__init__(session, Payment)
