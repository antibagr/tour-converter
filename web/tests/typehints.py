from typing import List
from _io import TextIOWrapper

from _pytest.main import Session  # Session Type
from django.contrib.auth import get_user_model
from django.core.mail.message import EmailMultiAlternatives as Mail
from django.test import Client  # Client fixture type
from factory.base import FactoryMetaClass as Factory  # Fake data factory
from py._path.local import LocalPath
from pytest_mock import MockerFixture

Mailbox = List[Mail]

User = get_user_model()
