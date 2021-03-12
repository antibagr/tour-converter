import pytest

from tests.typehints import Client, Factory


@pytest.fixture
def authorized_client(client: Client, user_factory: Factory) -> Client:
    " Return client authorized with profile factory "

    client.force_login(user_factory())
    return client
