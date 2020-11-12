"""Basic app tests"""


def test_home_page(test_app):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_app.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_hello_page(test_app):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    name = "John"
    response = test_app.get('/hello/'+name)
    assert response.status_code == 200
    hello_string = "Why Hello " + name
    assert bytes(hello_string, 'ascii') in response.data

