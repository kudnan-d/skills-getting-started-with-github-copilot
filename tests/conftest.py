import pytest
from fastapi.testclient import TestClient
from copy import deepcopy

from src.app import app, activities as _activities


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI app and restore in-memory state after each test."""
    original = deepcopy(_activities)
    with TestClient(app) as c:
        yield c

    # restore original activities state to keep tests isolated
    _activities.clear()
    _activities.update(original)
