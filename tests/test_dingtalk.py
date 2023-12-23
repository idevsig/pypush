import os

import pytest

from ipush.notify.dingtalk import Dingtalk


@pytest.fixture
def assess_token():
    token = os.environ.get('DingtalkToken')
    secret = os.environ.get('DingtalkSecret')
    return token, secret


@pytest.mark.skipif(
    not os.environ.get('DingtalkToken'), reason='Dingtalk Token not provided'
)
def test_dintalk(assess_token):
    token, secret = assess_token
    notify = Dingtalk(token, secret)
    res = notify.send('pypush test')
    json = res.json()
    assert json['errcode'] == 0
