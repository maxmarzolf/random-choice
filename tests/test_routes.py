from tests.create_client import client, client_no_db


def login(client, email, password):
    return client.post('/login', data=dict(email=email, password=password), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


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


# Login Routes
def test_login_w_db(client):
    with client:
        res = login(client, 'test@test.com', 'password')
        assert(b'Your Account' in res.data)

    lg = logout(client)
    assert b'<div class="post">' in lg.data


def test_logout_w_db(client):
    res = login(client, 'test@test.com', 'password')
    res = logout(client)
    assert b'<div class="post">' in res.data


# def test_login_no_db(client_no_db):
#     res = login(client_no_db, 'test@test.com', 'password')
#     assert b'Login</button>' in res.data