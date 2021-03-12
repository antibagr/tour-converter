from tests.factories.user import UserFactory


ALL = [UserFactory]

__all__ = [str(x.__name__) for x in ALL]
