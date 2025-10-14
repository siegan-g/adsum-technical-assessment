from sqlmodel import Field
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone
from infrastructure.database.repositories.base import OpenTaxEntity, GenericSqlRepository

class Logs(OpenTaxEntity, table=True):
    # IGNORE: Unfortunatetly pylance/pyright doesn't play nicely with __tablename__ definitions without a hacky workaround
    # https://github.com/fastapi/sqlmodel/issues/98
    __tablename__: str = "logs"  # type: ignore
    level: str = Field(max_length=20, nullable=False)
    message: str = Field(nullable=False)
    timestamp: datetime = Field(default=datetime.now(timezone.utc), nullable=False)

class LogsFilter(BaseModel):
    # Ensure BaseModel is implemented to keep a seperation of means of concern. This model should exist only on the application layer
    """
    Class with relevant filters for the Payment Class. 
    """
    from_date:Optional[datetime] = None
    to_date:Optional[datetime] = None
    level:Optional[str] = None
    offset:Optional[int] = None
    limit:Optional[int] = None
    