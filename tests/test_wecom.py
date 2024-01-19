import os

import pytest

from ipush import WeCom


@pytest.fixture
def access_token():
    token = os.environ.get('WeComToken')
    return token


@pytest.mark.skipif(not os.environ.get('WeComToken'), reason='WeCom Token not provided')
def test_wecom(access_token, message):
    token = access_token
    notify = WeCom(token)
    res = notify.send(message)
    assert res.status_code == 200
    json = res.json()
    assert json['errcode'] == 0


@pytest.mark.skipif(not os.environ.get('WeComToken'), reason='WeCom Token not provided')
def test_wecom_markdown(access_token, markdown_message):
    token = access_token
    notify = WeCom(token)
    res = notify.setmsgtype('markdown').send(markdown_message)
    assert res.status_code == 200
    json = res.json()
    assert json['errcode'] == 0
