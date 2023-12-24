import os

import pytest

from ipush.notify.feishu import Feishu


@pytest.fixture
def access_token():
    token = os.environ.get('FeishuToken')
    secret = os.environ.get('FeishuSecret')
    return token, secret


@pytest.mark.skipif(
    not os.environ.get('FeishuToken'), reason='Feishu Token not provided'
)
def test_feishu(access_token):
    token, secret = access_token
    notify = Feishu(token, secret)
    res = notify.send('pypush test')
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 0
