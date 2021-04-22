import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    client = app.test_client()
    yield client


def test_home(client):
    assert client.get('/').status_code == 200


def test_me(client):
    assert client.get('/post/1').status_code == 200