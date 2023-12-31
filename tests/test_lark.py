import os

import pytest

from ipush import Lark


@pytest.fixture
def access_token():
    token = os.environ.get('LarkToken')
    secret = os.environ.get('LarkSecret')
    return token, secret


@pytest.mark.skipif(not os.environ.get('LarkToken'), reason='Lark Token not provided')
def test_lark(access_token, message):
    token, secret = access_token
    notify = Lark(token, secret)
    res = notify.send(message)
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 0
