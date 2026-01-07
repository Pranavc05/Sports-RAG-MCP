from fastapi import FastAPI

from .config import settings
from .routers import health


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    app.include_router(health.router, tags=["system"])
    return app


app = create_app()

