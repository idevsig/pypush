import os

import pytest

from ipush import Alertzy


@pytest.fixture
def access_token():
    token = os.environ.get('AlertzyToken')
    return token


@pytest.mark.skipif(
    not os.environ.get('AlertzyToken'), reason='Alertzy Token not provided'
)
def test_alertzy(access_token, message):
    token = access_token
    notify = Alertzy(token)
    res = notify.send(message)
    assert res.status_code == 200
    json = res.json()
    assert json['response'] == 'success'


@pytest.mark.skipif(
    not os.environ.get('AlertzyToken'), reason='Alertzy Token not provided'
)
def test_alertzy_title(access_token, title, message):
    token = access_token
    notify = Alertzy(token)
    res = notify.send(message, title)
    assert res.status_code == 200
    json = res.json()
    assert json['response'] == 'success'
