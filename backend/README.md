# Backend

FastAPI service plus workers. Key modules:
- `app/` API endpoints (slate, game detail, odds, analyze, picks, user stats).
- `services/` orchestration, decision engine, provider clients (stats, odds, injuries).
- `workers/` Celery/RQ tasks for ingestion and backtesting.
- `schemas/` Pydantic models for requests/responses.
- `db/` SQLAlchemy models, migrations.

## Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e .

cp env.example .env  # fill in provider keys locally (do not commit)
```

## Run API (dev)

```bash
cd backend
./scripts/run_api.sh
# or
PYTHONPATH=backend uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

