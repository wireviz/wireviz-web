test:
	poetry run poe test

test-coverage:
	poetry run poe coverage

format:
	poetry run poe style

release:
	poetry run poe release --bump=$(bump)
