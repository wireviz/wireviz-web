###################
Release WireViz-Web
###################

1. Format code style::

    poe style
    git commit -a "Code style"

2. Bump minor version, tag repository and upload to PyPI::

   poe release --bump=minor
