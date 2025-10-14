"""Dependency injection container for the application."""
from sqlmodel import SQLModel
from application.logging.logger import Logger
from application.logging.loguru_logger import LoguruLogger
from application.settings import Settings
from infrastructure.database.session import create_sqlmodel_engine
from application.services.payments import PaymentsService
from application.services.invoices import InvoicesService
from application.services.logs import LogsService
from application.services.summary import SummaryService

def get_settings() -> Settings:
    return Settings()

def get_logger() -> Logger:
    settings = get_settings()
    app_settings = settings.get_app_settings()
    return LoguruLogger(app_settings)

def get_engine():
    settings = get_settings()
    db_settings = settings.get_db_settings()
    engine = create_sqlmodel_engine(db_settings['url'])
    SQLModel.metadata.create_all(engine)
    return engine

def get_payments_service() -> PaymentsService:
    return PaymentsService(engine=get_engine(), logger=get_logger())

def get_invoices_service() -> InvoicesService:
    return InvoicesService(engine=get_engine(), logger=get_logger())

def get_logs_service() -> LogsService:
    return LogsService(engine=get_engine(), logger=get_logger())

def get_summary_service() -> SummaryService:
    return SummaryService(engine=get_engine(), logger=get_logger())