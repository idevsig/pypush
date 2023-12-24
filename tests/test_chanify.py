import os

import pytest

from ipush.notify.chanify import Chanify


@pytest.fixture
def access_token():
    token = os.environ.get('ChanifyToken')
    custom_url = os.environ.get('ChanifyCustomURL')
    return token, custom_url


@pytest.mark.skipif(
    not os.environ.get('ChanifyToken'), reason='Chanify Token not provided'
)
def test_chanify(access_token):
    token, _ = access_token
    notify = Chanify(token)
    res = notify.send('pypush test')
    assert res.status_code == 200


@pytest.mark.skipif(
    not os.environ.get('ChanifyToken') or not os.environ.get('ChanifyCustomURL'),
    reason='Chanify Token not provided',
)
def test_chanify_custom_url(access_token):
    token, custom_url = access_token
    notify = Chanify(token)
    notify.seturl(custom_url)
    res = notify.send('pypush test custom url')
    assert res.status_code == 200
