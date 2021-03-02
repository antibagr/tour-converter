from typing import List
from account.models import Teacher


class BaseException(Exception):
    pass


class NoFreeSlots(BaseException):

    def __init__(self, teachers: List[Teacher], *args, **kw):
        self.teachers = teachers
        super().__init__(*args, **kw)


class NoSuchPortfolio(BaseException):
    pass
