from logger import Logger
from loguru import logger
from typing import Any
from sys import stdout


class LoguruLogger(Logger):
    def __init__(self, settings: dict[str, Any]) -> None:
        self.settings = settings
        sink = settings.get("sink", stdout)
        colorizer = True if sink == stdout else False
        level = settings.get("level", "DEBUG")
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
