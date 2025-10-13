from sqlmodel import create_engine, Session
from sqlalchemy import Engine
from typing import Callable


def create_sqlmodel_engine(connection_string:str)->Engine:
    return create_engine(connection_string,pool_pre_ping=True)


def session_factory(engine: Engine) -> Callable[[], Session]:
    return lambda: Session(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)
