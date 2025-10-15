from typing import Iterator
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from presentation.api.main import app as fastapi_app


@pytest.fixture(scope="session")
def app() -> FastAPI:
    return fastapi_app


@pytest.fixture
def client(app: FastAPI) -> Iterator[TestClient]:
    with TestClient(app=app) as tc:
        yield tc
