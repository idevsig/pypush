import os

import pytest

from ipush.notify.pushdeer import PushDeer


@pytest.fixture
def access_token():
    token = os.environ.get('PushDeerToken')
    custom_url = os.environ.get('PushDeerCustomURL')
    return token, custom_url


@pytest.mark.skipif(
    not os.environ.get('PushDeerToken'), reason='PushDeer Token not provided'
)
def test_PushDeer(access_token):
    token, _ = access_token
    notify = PushDeer(token)
    res = notify.send('pypush test')
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 0


@pytest.mark.skipif(
    not os.environ.get('PushDeerToken') or not os.environ.get('PushDeerCustomURL'),
    reason='PushDeer Token not provided',
)
def test_PushDeer_custom_url(access_token):
    token, custom_url = access_token
    notify = PushDeer(token)
    notify.seturl(custom_url)
    res = notify.send('pypush test custom url')
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 0
