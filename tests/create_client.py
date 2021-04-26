import pytest

from app import create_app
import config


@pytest.fixture
def client():
    app = create_app(config=config.Test())
    app.testing = True
    app.config['WTF_CSRF_ENABLED'] = False
    client = app.test_client()
    yield client


@pytest.fixture
def development_client():
    app = create_app(config=config.Development())
    app.testing = True
    app.config['FLASK_ENV'] = 'development'
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    client = app.test_client()
    yield client


@pytest.fixture
def production_client():
    app = create_app(config=config.Production())
    app.testing = True
    app.config['FLASK_ENV'] = 'production'
    app.config['ENV'] = 'production'
    app.config['DEBUG'] = False
    client = app.test_client()
    yield client


@pytest.fixture
def client_no_db():
    app = create_app(config=config.Test(no_db=True))
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            yield client
