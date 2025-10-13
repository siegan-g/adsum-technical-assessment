from sqlmodel import create_engine, Session
from sqlalchemy import Engine
from typing import Any, Callable


def create_sqlmodel_engine(connection_string:str)->Engine:
    return create_engine(connection_string)


def session_factory(engine: Engine) -> Callable[[], Session]:
    return lambda: Session(bind=engine, autocommit=False, autoflush=False)
