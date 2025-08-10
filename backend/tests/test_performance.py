# backend/tests/test_performance.py
import pytest
import time

@pytest.mark.performance
async def test_response_time(client):
    start = time.time()
    for _ in range(10):
        response = client.post(
            "/ask",
            json={"question": "Stress test", "user_id": 1}
        )
        assert response.status_code == 200
    duration = time.time() - start
    assert duration < 2.0  # 10 requests in under 2 seconds