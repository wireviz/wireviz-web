###################
Release WireViz-Web
###################

1. Format code::

    make format
    git commit -a -m "Format code"

2. Update ``CHANGES.rst``::

    git commit -a -m "Update changelog"

3. Bump minor version, tag repository and upload to PyPI::

    make release bump=minor

