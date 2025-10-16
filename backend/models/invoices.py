from sqlmodel import Field # type: ignore
from pydantic import BaseModel
from decimal import Decimal
from typing import Optional, List
from datetime import datetime, timezone
from infrastructure.database.repositories.base import OpenTaxEntity 

class Invoice(OpenTaxEntity, table=True):
    # IGNORE: Unfortunatetly pylance/pyright doesn't play nicely with __tablename__ definitions without a hacky workaround
    # https://github.com/fastapi/sqlmodel/issues/98
    __tablename__: str = "invoices"  # type: ignore
    amount: Decimal = Field(default=0, max_digits=10, decimal_places=2, nullable=False)
    currency: str = Field(default="GBP", max_length=3, nullable=False)
    status: str = Field(default="pending", max_length=20, nullable=False)
    due_date: datetime = Field(default=datetime.now(timezone.utc), nullable=False)
    client: str = Field(default="", max_length=100, nullable=False)
    timestamp: datetime = Field(default=datetime.now(timezone.utc), nullable=False)

class InvoiceFilter(BaseModel):
    # Ensure BaseModel is implemented to keep a seperation of means of concern. This model should exist only on the application layer
    """
    Class with relevant filters for the Invoice Class. 
    """
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None
    status: Optional[str] = None

class InvoicePaginate(BaseModel):
    offset: Optional[int] = None
    limit: Optional[int] = None

class InvoiceResponse(BaseModel):
    invoices: Optional[List[Invoice]] = None
    invoice_filter: Optional[InvoiceFilter] = None
    invoice_paginate: Optional[InvoicePaginate] = None
    count: Optional[int] = 0
