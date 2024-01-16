import os

import pytest

from ipush import Juhe


@pytest.fixture
def access_token():
    token = os.environ.get('JuheToken')
    service_id = os.environ.get('JuheServiceID')
    return token, service_id


@pytest.mark.skipif(
    not os.environ.get('JuheToken') or not os.environ.get('JuheServiceID'),
    reason='Juhe Token not provided',
)
def test_juhe(access_token, message):
    token, service_id = access_token
    notify = Juhe(token, service_id)
    res = notify.send(message)
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200


@pytest.mark.skipif(
    not os.environ.get('JuheToken') or not os.environ.get('JuheServiceID'),
    reason='Juhe Token not provided',
)
def test_juhe_title(access_token, title, message):
    token, service_id = access_token
    notify = Juhe(token, service_id)
    res = notify.send(message, title)
    assert res.status_code == 200
    json = res.json()
    assert json['code'] == 200
