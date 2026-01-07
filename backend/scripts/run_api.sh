#!/usr/bin/env bash
set -euo pipefail

# Start the FastAPI dev server.
# Usage: ./scripts/run_api.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${PROJECT_ROOT}"

# Ensure virtualenv is activated before running this.
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH:-}"

exec uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

