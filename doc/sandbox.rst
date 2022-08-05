####################
Sandbox installation
####################


************
Introduction
************

The project uses the `Poetry`_ dependency and package manager.


*******
Sandbox
*******

Install prerequisites::

    {apt,brew,yum,zypper} install python3 graphviz poetry

Setup development sandbox::

    git clone https://github.com/daq-tools/wireviz-web
    cd wireviz-web
    poetry install


*****
Tests
*****

Invoke tests, optionally with coverage report::

    # Run tests
    poetry run poe test

    # Run tests, with coverage
    poetry run poe coverage


***********
Maintenance
***********

In order to update Poetry's lock file without upgrading dependencies, invoke::

    poetry lock --no-update

In order to upgrade dependencies, invoke::

    poetry update
