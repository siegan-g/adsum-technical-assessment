import pytest


@pytest.mark.anyio
async def test_health_ok(client):
    response = await client.get("/api/health/")
    assert response.status_code == 200
    assert response.json() == {"status": True}

