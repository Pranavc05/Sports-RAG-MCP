# Sports RAG + MCP

NBA betting analytics web app built with an agentic backend (MCP tools) plus FastAPI, designed to expand to other sports. Goal: actionable, evidence-backed recommendations (pick/no pick, confidence, edge, key drivers, citations, tracking).

## Working Model
- Branch strategy: feature branches → PRs to `main`. Current: `feat/nba-mvp-foundation`.
- Commits: small, frequent.
- Deploy targets (initial): Backend/worker on Render or Fly.io; frontend on Vercel.
- Auth (MVP): Clerk (can swap to Supabase Auth if you prefer single Postgres).

## MVP Provider Choices
- LLM + embeddings: OpenAI (chat + embeddings). Easy swap path to Anthropic/Cohere/local.
- Stats + injuries: SportsDataIO (stable NBA coverage). Pluggable adapter interface for future providers.
- Odds: TheOddsAPI (moneyline focus to start). Supports line movement snapshots.
- DB: Managed Postgres + pgvector (one cluster). 
- Cache/queue: Redis (Upstash/managed) + Celery/RQ workers.
- Storage: S3/R2 later if needed for artifacts.
- Observability: Sentry for errors; structured logs.

## Initial Scope (Phase 1 MVP)
- Game query: NBA moneyline recommendations with odds, win prob, implied prob, EV, pick/no-pick, rationale, citations.
- Data ingestion: schedules, teams, players, odds snapshots, injuries/news (for RAG).
- Modeling: baseline win-prob model (ratings, form, rest, injuries); EV/edge calculation.
- RAG: ingest news/injury text → embeddings in pgvector → filtered retrieval by team/date.
- Agent/LLM: orchestrate tool calls (stats/odds/news) and generate structured report JSON for UI.
- User features: auth, save picks, simple dashboard (ROI/hit rate), pick tracking.

## Core Components (sport-agnostic design)
- `backend/` FastAPI service: REST endpoints, auth, orchestration, Celery tasks.
- `data/` ingestion jobs + provider adapters (stats, injuries, odds).
- `model/` feature generation + probability + calibration + backtesting utilities.
- `rag/` ingestion, embeddings, retrieval service (pgvector).
- `frontend/` web app (Next.js/React) consuming API.
- `infra/` IaC/config (env templates, deploy manifests).

## Disclaimers (MVP copy)
- Informational/entertainment only. Not financial advice. No guarantees.
- 21+ where legal; comply with local laws and operator rules.
- Odds and lines subject to change; recommendations depend on data freshness.

## Near-Term Tasks
- Scaffold backend/frontend/infra directories.
- Add env templates and provider config stubs.
- Define DB schema (Postgres + pgvector) and migrations.
- Implement ingestion adapters (SportsDataIO, TheOddsAPI) with caching and rate limiting.
- Baseline model + EV engine; calibration hooks.
- RAG ingestion + retrieval with metadata filters.
- API endpoints: slate, game detail, odds, analyze, picks, user stats.
- Basic UI pages: landing, slate, game detail, analyze prompt, picks dashboard.

