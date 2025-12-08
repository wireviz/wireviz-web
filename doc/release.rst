###################
Release WireViz-Web
###################

1. Format code::

    make format
    git commit -a -m "Format code"

2. Update ``CHANGES.rst``::

    git commit -a -m "Update changelog"

3. Tag repository, push to remote, and upload to PyPI::

    git tag 0.4.2
    git push && git push --tags
    python -m build
    twine upload dist/*
