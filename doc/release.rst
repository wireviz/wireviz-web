###################
Release WireViz-Web
###################

1. Format code style::

    poe style
    git commit -a "Code style"

2. Bump minor version, tag repository and upload to PyPI::

    make release

   Bump other steps::

    make release bump=patch

