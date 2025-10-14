from application.logging.logger import Logger
from application.logging.db_sink import database_sink
from loguru import logger
from typing import Any
from sys import stdout


class LoguruLogger(Logger):
    def __init__(self, settings: dict[str, Any]) -> None:
        self.settings = settings
        if settings.get("sink", "stdout") == "database":
            sink = database_sink
        else:
            sink = stdout
            
        colorizer = True if sink == stdout else False
        
        level = "DEBUG" if settings.get("debug", True) == True else "INFO" 
        # Standard practice to remove all handlers before adding a new one
        logger.remove()
        logger.add(sink, colorize=colorizer, level=level)

    def debug(self, msg: str) -> None:
        logger.debug(msg)

    def info(self, msg: str) -> None:
        logger.info(msg)

    def warning(self, msg: str) -> None:
        logger.warning(msg)

    def error(self, msg: str) -> None:
        logger.error(msg)
