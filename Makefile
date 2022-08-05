install:
	poetry install

test: install
	poetry run poe test

test-coverage: install
	poetry run poe coverage

format: install
	poetry run poe style

release: install
	poetry run poe release --bump=$(bump)
