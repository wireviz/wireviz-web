default:
	@#

release:
	$(eval bump ?= minor)
	poetry version $(bump)
	$(eval version := $(shell poetry version --short))
	git commit pyproject.toml -m "Bump version to $(version)"
	git tag $(version)
	git push && git push --tags
	poetry build && poetry publish
