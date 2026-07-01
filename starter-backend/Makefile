.PHONY: install run test lint typecheck

install:
	uv sync --extra dev

run:
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir src

test:
	uv run pytest

lint:
	uv run ruff check .

typecheck:
	uv run mypy src
