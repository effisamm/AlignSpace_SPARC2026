import pytest

@pytest.fixture
def api_client():
    """Fixture for API testing"""
    from fastapi.testclient import TestClient
    from main import app
    return TestClient(app)
