###################
Release WireViz-Web
###################

1. Improve code style::

    make format
    git commit -a -m "Code style"

2. Update ``CHANGES.rst``::

    git commit -a -m "Update changelog"

3. Bump minor version, tag repository and upload to PyPI::

    make release bump=minor

