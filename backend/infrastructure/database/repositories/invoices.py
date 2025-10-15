from infrastructure.database.repositories.base import GenericSqlRepository

from models.invoices import Invoice

class InvoiceRepository(GenericSqlRepository[Invoice]):
    def __init__(self, session):
        super().__init__(session, Invoice)
