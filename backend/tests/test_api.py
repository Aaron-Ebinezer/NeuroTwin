# backend/tests/test_api.py
import pytest
from fastapi import status

@pytest.mark.asyncio
async def test_ask_endpoint_success(client):
    response = client.post(
        "/ask",
        json={"question": "Explain photosynthesis", "user_id": 1}
    )
    assert response.status_code == status.HTTP_200_OK
    assert "answer" in response.json()
    assert "tier" in response.json()

@pytest.mark.asyncio
@pytest.mark.parametrize("payload,expected_status", [
    ({"user_id": 1}, status.HTTP_422_UNPROCESSABLE_ENTITY),  # Missing question
    ({"question": "", "user_id": 1}, status.HTTP_422_UNPROCESSABLE_ENTITY),
    ({"question": "   ", "user_id": 1}, status.HTTP_422_UNPROCESSABLE_ENTITY),
    ({"question": "test", "user_id": 999}, status.HTTP_404_NOT_FOUND),
])
async def test_ask_endpoint_failures(client, payload, expected_status):
    response = client.post("/ask", json=payload)
    assert response.status_code == expected_status