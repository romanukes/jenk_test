"""Used to setup fixtures to be used through tests"""
import pytest
from helloworld_flask import app

@pytest.fixture()
def give_me_success():
    """
    Provides True to make tests pass

    Returns:
        (bool): Returns True
    """
    return True

@pytest.fixture()
def test_app():
    app_ = app.create_app()
    return app_.test_client()