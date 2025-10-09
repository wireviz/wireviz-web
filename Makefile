install:
	uv pip install --editable=. --group=dev

test: install
	uv run poe test

test-coverage: install
	uv run poe coverage

format: install
	uv run poe format

release: install
	uv run poe release --bump=$(bump)
