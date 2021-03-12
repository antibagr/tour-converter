import pytest
from pytest_factoryboy import register
from tests import factories, fixtures
from tests.typehints import Session
from tests.walk_packages import get_package_paths_in_module


@pytest.hookimpl()
def pytest_sessionstart(session: Session) -> None:

    print("Start testing")

# Load fixtures


pytest_plugins = [
    *get_package_paths_in_module(fixtures),
]


for factory in factories.ALL:
    register(factory)
