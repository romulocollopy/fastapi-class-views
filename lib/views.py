from starlette.responses import JSONResponse
from starlette import status


class View:

    ALLOWED_METHODS = [
        "POST",
        "GET",
        "PUT",
        "DELETE",
        "OPTIONS",
        "HEAD",
        "PATCH",
        "TRACE",
    ]

    @classmethod
    def handles_path(cls, path, *args, **kwargs):
        from lib.router import class_router
        class_router.register(path, cls(), *args, **kwargs)
        return class_router.engine
