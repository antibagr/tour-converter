from django.core.handlers.wsgi import WSGIRequest
from django.core.handlers.asgi import ASGIRequest
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from typing import TypeVar, Union


__all__ = ['RequestType', 'HttpRequest', 'HttpResponse']


RequestType = TypeVar("Request", bound=Union[WSGIRequest, ASGIRequest])
