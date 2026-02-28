src := "structy"

# show this help message (default)
help:
    @just -l

# format with ruff
fmt:
    uv run ruff check --fix {{src}}
    uv run ruff format {{src}}

# lint with ruff and type-check with ty
lint:
    uv run ruff check {{src}}
    uv run ruff format --check {{src}}
    uv run ty check {{src}}

# run tests with pytest
test:
    uv run pytest {{src}}/*.py
