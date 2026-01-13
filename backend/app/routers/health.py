from fastapi import APIRouter

from ..config import settings

router = APIRouter()


@router.get("/health", summary="Liveness probe")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/ready", summary="Readiness probe")
async def ready() -> dict[str, str]:
    # In a fuller implementation, check DB/cache/provider connectivity.
    return {"status": "ready"}


@router.get("/version", summary="Version info")
async def version() -> dict[str, str]:
    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }

