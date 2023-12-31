import os

import pytest

from ipush import Notify


@pytest.fixture
def access_token():
    token = os.environ.get('NotifyToken')
    user_id = os.environ.get('NotifyUserId')
    return token, user_id


@pytest.mark.skipif(
    not os.environ.get('NotifyToken') or not os.environ.get('NotifyUserId'),
    reason='Notify Token not provided',
)
def test_notify(access_token, message):
    token, user_id = access_token
    notify = Notify(token, user_id)
    res = notify.send(message)
    assert res.status_code == 200
    json = res.json()
    assert json['notification_id'] != ''


@pytest.mark.skipif(
    not os.environ.get('NotifyToken') or not os.environ.get('NotifyUserId'),
    reason='Notify Token not provided',
)
def test_notify_title(access_token, message, title):
    token, user_id = access_token
    notify = Notify(token, user_id)
    res = notify.send(message, title)
    assert res.status_code == 200
    json = res.json()
    assert json['notification_id'] != ''
