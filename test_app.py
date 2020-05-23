import os
import tempfile

import pytest

from app import create_app, db

with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")

@pytest.fixture
def app():
# create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app({"TESTING": True, "DATABASE": db_path})

    # create the database and load test data
    with app.app_context():
        #init_db()
        #get_db().executescript(_data_sql)
        print("running tests.")

    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_bad_url(client):

    rv = client.get("/something")
    assert b'Not Found' in rv.data