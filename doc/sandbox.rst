####################
Sandbox installation
####################


************
Introduction
************

The project uses the `uv`_ package and project manager.


*******
Sandbox
*******

Install prerequisites::

    {apt,brew,yum,zypper} install python3 graphviz
    pip install uv

Setup development sandbox::

    git clone https://github.com/wireviz/wireviz-web
    cd wireviz-web
    uv venv --python 3.13 --seed .venv
    source .venv/bin/activate
    uv pip install --editable=. --group=dev


*****
Tests
*****

Invoke tests, optionally with coverage report::

    # Run tests
    uv run poe test

    # Run tests, with coverage
    uv run poe coverage


***********
Maintenance
***********

In order to update uv's lock file, invoke::

    uv lock


.. _uv: https://docs.astral.sh/uv/
