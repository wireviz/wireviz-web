default:
	@#

release:
	git push && git push --tags
	poetry build && poetry publish
