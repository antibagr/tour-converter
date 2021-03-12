import pytest
from tests.typehints import User


@pytest.fixture
def person() -> User:
    " Return created profile or raise RuntimeError "

    if not User.objects.count():
        raise RuntimeError("No profile were created still")

    return User.objects.first()
