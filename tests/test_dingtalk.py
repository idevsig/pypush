import os

import pytest

from ipush.notify.dingtalk import Dingtalk


@pytest.fixture
def access_token():
    token = os.environ.get('DingtalkToken')
    secret = os.environ.get('DingtalkSecret')
    return token, secret


@pytest.mark.skipif(
    not os.environ.get('DingtalkToken'), reason='Dingtalk Token not provided'
)
def test_dintalk(access_token):
    token, secret = access_token
    notify = Dingtalk(token, secret)
    res = notify.send('pypush test')
    assert res.status_code == 200
    json = res.json()
    assert json['errcode'] == 0
