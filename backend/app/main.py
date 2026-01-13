from fastapi import FastAPI

from .config import settings
from .logging import add_request_logging, configure_logging
from .routers import health


def create_app() -> FastAPI:
    configure_logging(settings.log_level)

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    add_request_logging(app)
    app.include_router(health.router, tags=["system"])
    return app


app = create_app()

