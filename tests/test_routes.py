from tests.create_client import client, client_no_db


def test_home(client):
    assert client.get('/').status_code == 200


def test_read_post(client):
    assert client.get('/post/1').status_code == 200
    assert client.get('/post/2').status_code == 200
    assert client.get('/post/3').status_code == 200
    assert client.get('/post/4').status_code == 200


def test_no_db(client_no_db):
    assert client_no_db.get('/post/1').status_code == 200