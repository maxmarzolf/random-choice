from tests.create_client import client, client_no_db


def test_home(client):
    assert client.get('/').status_code == 200


def test_read_post(client):
    assert client.get('/post/1').status_code == 200
    assert client.get('/post/2').status_code == 200
    assert client.get('/post/3').status_code == 200
    assert client.get('/post/4').status_code == 200


def test_home_no_posts_no_db(client_no_db):
    res = client_no_db.get('/')
    assert b'Could not retrieve posts.' in res.data


def test_home_no_post_no_db(client_no_db):
    res = client_no_db.get('/post/1')
    assert b'Could not retrieve post.' in res.data