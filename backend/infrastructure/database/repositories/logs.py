from infrastructure.database.repositories.base import GenericSqlRepository
from models.logs import Logs

class LogsRepository(GenericSqlRepository[Logs]):
    def __init__(self, session):
        super().__init__(session, Logs)