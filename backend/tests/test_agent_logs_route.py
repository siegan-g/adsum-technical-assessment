from datetime import datetime, timezone
import pytest
from fastapi import FastAPI

from application.dependency_container import get_agent_logs_service, get_settings
from application.services.logs import AgentLogsService
from application.settings import Settings
from models.logs import Logs, LogsResponse, LogsFilter, LogsPaginate


class _StubAgentLogsService(AgentLogsService):
    def __init__(self):  
        pass

    def read(self, paginate, **filters): 
        return [
            Logs(
                id=1,
                level="INFO",
                message="Test log message 1",
                timestamp=datetime.now(timezone.utc),
            ),
            Logs(
                id=2,
                level="ERROR",
                message="Test log message 2",
                timestamp=datetime.now(timezone.utc),
            ),
        ]
    
    def count(self, **filters):
        return 2


def test_agent_logs_limit_exceeds_returns_400(client):
    settings: Settings = get_settings()
    max_limit = settings.get_app_settings()["max_limit"]

    response = client.get(f"/api/agent-logs/?limit={max_limit + 1}")
    assert response.status_code == 400


def test_agent_logs_returns_response_when_ok(app: FastAPI, client):
    app.dependency_overrides[get_agent_logs_service] = lambda: _StubAgentLogsService()
    try:
        response = client.get("/api/agent-logs/?limit=2")
        assert response.status_code == 200
        data = response.json()
        
        # Test the new response structure
        assert "logs" in data
        assert "logs_filter" in data
        assert "logs_paginate" in data
        assert "count" in data
        
        # Test logs data
        logs = data["logs"]
        assert isinstance(logs, list)
        assert len(logs) == 2
        assert {item["level"] for item in logs} == {"INFO", "ERROR"}
        
        # Test pagination data
        assert data["count"] == 2
        assert data["logs_paginate"]["limit"] == 2
        
        # Test filter data
        assert data["logs_filter"] is not None
    finally:
        app.dependency_overrides.pop(get_agent_logs_service, None)


def test_agent_logs_with_filters(app: FastAPI, client):
    app.dependency_overrides[get_agent_logs_service] = lambda: _StubAgentLogsService()
    try:
        response = client.get("/api/agent-logs/?level=INFO&limit=1")
        assert response.status_code == 200
        data = response.json()
        
        # Test that filters are properly passed
        assert data["logs_filter"]["level"] == "INFO"
        assert data["logs_paginate"]["limit"] == 1
    finally:
        app.dependency_overrides.pop(get_agent_logs_service, None)