import os

import pytest

from ipush import Bark


@pytest.fixture
def access_token():
    token = os.environ.get('BarkToken')
    custom_url = os.environ.get('BarkCustomURL')
    return token, custom_url


@pytest.mark.skipif(not os.environ.get('BarkToken'), reason='Bark Token not provided')
def test_bark(access_token, message):
    token, _ = access_token
    notify = Bark(token)
    res = notify.send(message)
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200


@pytest.mark.skipif(not os.environ.get('BarkToken'), reason='Bark Token not provided')
def test_bark_title(access_token, message, title):
    token, _ = access_token
    notify = Bark(token)
    res = notify.send(message, title)
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200


@pytest.mark.skipif(
    not os.environ.get('BarkToken') or not os.environ.get('BarkCustomURL'),
    reason='Bark Token not provided',
)
def test_bark_custom_url(access_token, custom_message):
    token, custom_url = access_token
    notify = Bark(token)
    notify.seturl(custom_url)
    res = notify.send(custom_message)
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200
