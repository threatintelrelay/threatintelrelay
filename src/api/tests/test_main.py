import os
import pytest
import httpx

API_URL = os.getenv("API_URL", "http://localhost:8000")

@pytest.mark.asyncio
async def test_root():
    async with httpx.AsyncClient(base_url=API_URL) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "ThreatIntelRelay MCP server is up!"}
