from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def debug(self, msg: str) -> None:
        raise NotImplementedError()

    def info(self, msg: str) -> None:
        raise NotImplementedError()

    def warning(self, msg: str) -> None:
        raise NotImplementedError()

    def error(self, msg: str) -> None:
        raise NotImplementedError()
