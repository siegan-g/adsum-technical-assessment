from application.logging.logger import Logger
from application.logging.custom_sink import DatabaseSink
# from application.dependency_container import get_agent_logs_service
from application.services.logs import AgentLogsService
from loguru import logger
from typing import Any
from sys import stdout


class LoguruLogger(Logger):
    def __init__(self, settings: dict[str, Any],log_service:AgentLogsService) -> None:
        self.settings = settings
        if settings.get("sink", "stdout") == "database":
            sink = DatabaseSink(log_service) 
        else:
            sink = stdout
            
        has_colorizer = True if sink == stdout else False
        
        level = "DEBUG" if settings.get("debug", True) == True else "INFO" 
        # Standard practice to remove all handlers before adding a new one
        logger.remove()
        logger.add(sink, colorize=has_colorizer, level=level)

    def debug(self, msg: str) -> None:
        logger.debug(msg)

    def info(self, msg: str) -> None:
        logger.info(msg)

    def warning(self, msg: str) -> None:
        logger.warning(msg)

    def error(self, msg: str) -> None:
        logger.error(msg)
