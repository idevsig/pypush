import os

import pytest

from ipush import Bark


@pytest.fixture
def access_token():
    token = os.environ.get('BarkToken')
    custom_url = os.environ.get('BarkCustomURL')
    return token, custom_url


@pytest.mark.skipif(not os.environ.get('BarkToken'), reason='Bark Token not provided')
def test_bark(access_token):
    token, _ = access_token
    notify = Bark(token)
    res = notify.send('pypush test')
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200


@pytest.mark.skipif(not os.environ.get('BarkToken'), reason='Bark Token not provided')
def test_bark_title(access_token):
    token, _ = access_token
    notify = Bark(token)
    res = notify.send('pypush test', 'ipush')
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200


@pytest.mark.skipif(
    not os.environ.get('BarkToken') or not os.environ.get('BarkCustomURL'),
    reason='Bark Token not provided',
)
def test_bark_custom_url(access_token):
    token, custom_url = access_token
    notify = Bark(token)
    notify.seturl(custom_url)
    res = notify.send('pypush test custom url')
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200
