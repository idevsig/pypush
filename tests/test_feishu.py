import os

import pytest

from ipush import Feishu


@pytest.fixture
def access_token():
    token = os.environ.get('FeishuToken')
    secret = os.environ.get('FeishuSecret')
    return token, secret


@pytest.mark.skipif(
    not os.environ.get('FeishuToken'), reason='Feishu Token not provided'
)
def test_feishu(access_token, message):
    token, secret = access_token
    notify = Feishu(token, secret)
    res = notify.send(message)
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 0
