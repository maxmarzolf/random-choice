from tests.create_client import production_client, development_client


def test_development_config(development_client):
    """Production config."""
    app = development_client
    assert app.application.config['ENV'] == 'development'
    assert app.application.config['DEBUG']


def test_production_config(production_client):
    """Development config."""
    app = production_client
    assert app.application.config['ENV'] == 'production'
    assert not app.application.config['DEBUG']