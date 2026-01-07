# Backend

FastAPI service plus workers. Key modules:
- `app/` API endpoints (slate, game detail, odds, analyze, picks, user stats).
- `services/` orchestration, decision engine, provider clients (stats, odds, injuries).
- `workers/` Celery/RQ tasks for ingestion and backtesting.
- `schemas/` Pydantic models for requests/responses.
- `db/` SQLAlchemy models, migrations.

