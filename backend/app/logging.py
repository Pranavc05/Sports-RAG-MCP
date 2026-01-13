import sys
import time

from fastapi import FastAPI, Request
from loguru import logger


def configure_logging(log_level: str = "INFO") -> None:
    """Configure loguru to log to stdout with a simple format."""
    logger.remove()
    logger.add(
        sys.stdout,
        level=log_level.upper(),
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | {level} | {message}",
        enqueue=True,
        backtrace=False,
        diagnose=False,
    )


def add_request_logging(app: FastAPI) -> None:
    """Add middleware to log each request with latency and status."""

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start) * 1000
        logger.info(
            "{method} {path} -> {status} ({duration_ms:.1f} ms)",
            method=request.method,
            path=request.url.path,
            status=response.status_code,
            duration_ms=duration_ms,
        )
        return response

