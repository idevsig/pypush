import pytest


@pytest.fixture
def title():
    return 'iPush'


@pytest.fixture
def message():
    return 'PyPush test'


@pytest.fixture
def custom_message():
    return 'PyPush test custom url'
