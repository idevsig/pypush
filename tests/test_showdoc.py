import os

import pytest

from ipush import Showdoc


@pytest.fixture
def access_token():
    token = os.environ.get('ShowdocToken')
    return token


@pytest.mark.skipif(
    not os.environ.get('ShowdocToken'), reason='Showdoc Token not provided'
)
def test_showdoc(access_token, message):
    token = access_token
    notify = Showdoc(token)
    res = notify.send(message)
    assert res.status_code == 200
    json = res.json()
    assert json['error_code'] == 0


@pytest.mark.skipif(
    not os.environ.get('ShowdocToken'), reason='Showdoc Token not provided'
)
def test_showdoc_title(access_token, message, title):
    token = access_token
    notify = Showdoc(token)
    res = notify.send(message, title)
    assert res.status_code == 200
    json = res.json()
    assert json['error_code'] == 0
