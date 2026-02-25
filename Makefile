.PHONY: all
all: fmt lint test

.PHONY: fmt
fmt:
	uv run ruff format structy

.PHONY: lint
lint:
	uv run ruff check --fix structy
	uv run ty check structy

.PHONY: check
check:
	uv run ruff format --check structy
	uv run ruff check structy
	uv run ty check structy

.PHONY: test
test:
	uv run pytest structy/*.py
