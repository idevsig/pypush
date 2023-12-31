import os

import pytest

from ipush import Telegram


@pytest.fixture
def access_token():
    token = os.environ.get('TelegramToken')
    chat_id = os.environ.get('TelegramChatId')
    custom_url = os.environ.get('TelegramCustomURL')
    return token, chat_id, custom_url


@pytest.mark.skipif(
    not os.environ.get('TelegramToken') or not os.environ.get('TelegramChatId'),
    reason='Telegram Token not provided',
)
def test_telegram(access_token, message):
    token, chat_id, _ = access_token
    notify = Telegram(token, chat_id)
    res = notify.send(message)
    assert res.status_code == 200
    json = res.json()
    assert json['ok']


@pytest.mark.skipif(
    not os.environ.get('TelegramToken')
    or not os.environ.get('TelegramChatId')
    or not os.environ.get('TelegramCustomURL'),
    reason='Telegram Token not provided',
)
def test_telegram_custom_url(access_token, custom_message):
    token, chat_id, custom_url = access_token
    notify = Telegram(token, chat_id)
    notify.seturl(custom_url)
    res = notify.send(custom_message)
    assert res.status_code == 200
    json = res.json()
    assert json['ok']
