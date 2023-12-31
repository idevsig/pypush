import os

import pytest

from ipush import PushPlus


@pytest.fixture
def access_token():
    token = os.environ.get('PushPlusToken')
    return token


@pytest.mark.skipif(
    not os.environ.get('PushPlusToken'), reason='PushPlus Token not provided'
)
def test_pushplus(access_token, message):
    token = access_token
    notify = PushPlus(token)
    res = notify.send(message)
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200


@pytest.mark.skipif(
    not os.environ.get('PushPlusToken'), reason='PushPlus Token not provided'
)
def test_pushplus_title(access_token, message, title):
    token = access_token
    notify = PushPlus(token)
    res = notify.send(message, title)
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200
