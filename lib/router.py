from functools import wraps
from lib.views import View
from fastapi import APIRouter


class ClassRouter:

    def __init__(self, engine=None, allowed_methods=None):
        self.engine = engine or APIRouter()
        self.allowed_methods = allowed_methods or View.ALLOWED_METHODS

    def register(self, path: str, func: View, *args, **kwargs) -> None:

        for method in self.allowed_methods:
            try:
                handler = getattr(func, method.lower())
            except AttributeError:
                continue

            self.engine.add_api_route(
                path=path,
                endpoint=handler,
                *args,
                methods=[method],
                **kwargs,
            )


class_router = ClassRouter()
