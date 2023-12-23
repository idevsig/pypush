import os

import pytest
from src.ipush.notify.feishu import Feishu


@pytest.fixture
def assess_token():
    token = os.environ.get('FeishuToken')
    secret = os.environ.get('FeishuSecret')
    return token, secret


@pytest.mark.skipif(
    not os.environ.get('FeishuToken'), reason='Feishu Token not provided'
)
def test_feishu(assess_token):
    token, secret = assess_token
    notify = Feishu(token, secret)
    res = notify.send('pypush test')
    json = res.json()
    assert json['code'] == 0
