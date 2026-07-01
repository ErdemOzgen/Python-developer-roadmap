# Starter Backend

This starter project is the first implementation step for the Python Backend Roadmap 2026.

## What is included

- FastAPI service skeleton
- Environment-based settings
- Health endpoint
- pytest test example
- Dockerfile and docker-compose stack with PostgreSQL and Redis
- Make targets for install, run, test, lint, and type checking

## Quick start

### Option A: uv workflow

```bash
uv sync --extra dev
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir src
```

### Option B: Docker workflow

```bash
docker compose up --build
```

Then open:
- http://localhost:8000/health
- http://localhost:8000/docs

## Local quality checks

```bash
uv run pytest
uv run ruff check .
uv run mypy src
```
