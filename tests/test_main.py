import pytest
from httpx import AsyncClient
from src.api.main import app

import pytest
import asyncio

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    # Optionally, check response content
    # assert response.json() == {"message": "Hello World"}
