import os

import pytest

from ipush.notify.xizhi import Xizhi


@pytest.fixture
def access_token():
    token = os.environ.get('XizhiToken')
    return token


@pytest.mark.skipif(not os.environ.get('XizhiToken'), reason='Xizhi Token not provided')
def test_xizhi(access_token):
    token = access_token
    notify = Xizhi(token)
    res = notify.send('pypush test')
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200


@pytest.mark.skipif(not os.environ.get('XizhiToken'), reason='Xizhi Token not provided')
def test_xizhi_title(access_token):
    token = access_token
    notify = Xizhi(token)
    res = notify.send('pypush test', 'ipush')
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200
