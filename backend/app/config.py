from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Sports RAG + MCP Backend"
    app_version: str = "0.1.0"
    environment: str = "local"
    log_level: str = "INFO"
    openai_api_key: str | None = None
    sportsdataio_api_key: str | None = None
    theoddsapi_api_key: str | None = None
    database_url: str = "postgresql+asyncpg://user:pass@localhost:5432/sportsrag"
    redis_url: str = "redis://localhost:6379/0"
    sentry_dsn: str | None = None
    clerk_publishable_key: str | None = None
    clerk_secret_key: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

