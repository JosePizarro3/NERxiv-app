"""Test the FastAPI backend."""

from fastapi.testclient import TestClient

from nerxiv_app._version import __version__
from nerxiv_app.backend.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Welcome to NERxiv API"
    assert data["version"] == __version__
    assert data["docs"] == "/docs"


def test_health_endpoint():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
