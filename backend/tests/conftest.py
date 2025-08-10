# backend/tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.models.user import User
from backend.services.database.session import AsyncSessionLocal

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
async def setup_test_db():
    """Auto-create test user before each test, clean up after"""
    async with AsyncSessionLocal() as session:
        test_user = User(
            id=1,
            username="test_user",
            password_hash="hashed_pass",
            tier="basic",
            initial_assessment=3.0
        )
        session.add(test_user)
        await session.commit()
        yield
        await session.delete(test_user)
        await session.commit()