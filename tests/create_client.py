import pytest

from app import create_app

import config


@pytest.fixture
def client():
    app = create_app(config=config.Test())
    app.testing = True
    client = app.test_client()
    yield client


@pytest.fixture
def client_no_db(config=config.Test()):
    app = create_app(config=config)

    with app.test_client() as client:
        with app.app_context():
            yield client