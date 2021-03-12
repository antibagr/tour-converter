import os
from pathlib import Path


import pytest
from unittest import mock


@pytest.fixture(autouse=True, scope='module')
def mock_recaptcha_environment():
    "Context manager with disabled RECAPTCHA"

    with mock.patch.dict(os.environ, {"RECAPTCHA_DISABLE": "True"}):
        yield


@pytest.fixture
def test_data_folder() -> Path:
    return Path(__file__).resolve().parent.parent / 'data'
