import copy
import pytest
from fastapi.testclient import TestClient
import src.app as app_module
from src.app import app


@pytest.fixture
def client():
    return TestClient(app, follow_redirects=False)


@pytest.fixture(autouse=True)
def reset_activities():
    # Arrange: snapshot global state before each test
    original = copy.deepcopy(app_module.activities)
    yield
    # Teardown: restore global state after each test
    app_module.activities.clear()
    app_module.activities.update(original)
