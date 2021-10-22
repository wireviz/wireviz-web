###################
Release WireViz-Web
###################

1. Improve code style::

    poe style
    git commit -a "Code style"

2. Update ``CHANGES.rst``.

3. Bump minor version, tag repository and upload to PyPI::

    poe release --bump=minor

