# -*- coding: utf-8 -*-
import app as test_app
import pytest


#@pytest.fixture
def test_route():
    with test_app.app.test_client() as c:
        response = c.get('/')
        assert b"Hello World!" == response.get_data()

        response = c.get('/duck')
        assert b"404 PAGE NOT FOUND" == response.get_data()

        response = c.get('/status')
        assert "OK - healthy" == response.get_json().get('result')

