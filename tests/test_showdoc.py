import os

import pytest

from ipush.notify.showdoc import Showdoc


@pytest.fixture
def access_token():
    token = os.environ.get('ShowdocToken')
    return token


@pytest.mark.skipif(
    not os.environ.get('ShowdocToken'), reason='Showdoc Token not provided'
)
def test_showdoc(access_token):
    token = access_token
    notify = Showdoc(token)
    res = notify.send('pypush test')
    assert res.status_code == 200
    json = res.json()
    assert json['error_code'] == 0


@pytest.mark.skipif(
    not os.environ.get('ShowdocToken'), reason='Showdoc Token not provided'
)
def test_showdoc_title(access_token):
    token = access_token
    notify = Showdoc(token)
    res = notify.send('pypush test', 'ipush')
    assert res.status_code == 200
    json = res.json()
    assert json['error_code'] == 0
