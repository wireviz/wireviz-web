###########
WireViz-Web
###########

.. image:: https://github.com/daq-tools/wireviz-web/workflows/Tests/badge.svg
    :target: https://github.com/daq-tools/wireviz-web/actions?workflow=Tests
.. image:: https://codecov.io/gh/daq-tools/wireviz-web/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/daq-tools/wireviz-web

.. image:: https://img.shields.io/pypi/v/wireviz-web.svg
    :target: https://pypi.org/project/wireviz-web/
.. image:: https://img.shields.io/github/v/tag/daq-tools/wireviz-web.svg
    :target: https://github.com/daq-tools/wireviz-web
.. image:: https://img.shields.io/pypi/dm/wireviz-web.svg
    :target: https://pypi.org/project/wireviz-web/

.. image:: https://img.shields.io/pypi/pyversions/wireviz-web.svg
    :target: https://pypi.org/project/wireviz-web/
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
.. image:: https://img.shields.io/pypi/status/wireviz-web.svg
    :target: https://pypi.org/project/wireviz-web/
.. image:: https://img.shields.io/github/license/daq-tools/wireviz-web
    :target: https://github.com/daq-tools/wireviz-web/blob/main/LICENSE


*****
About
*****
WireViz-Web is a wrapper around the excellent WireViz_ by `Daniel Rojas`_
for bringing it to the web.

Originally, it has been conceived within a `WireViz fork`_ by `Jürgen Key`_.
For compatibility with PlantUML_, it includes an URL query parameter decoder
by `Dyno Fu`_ and `Rudi Yardley`_.

Thanks!


*******
Details
*******

WireViz
=======
WireViz is a tool for easily documenting cables, wiring harnesses and connector pinouts.
It takes plain text, YAML-formatted files as input and produces beautiful graphical output
(SVG, PNG, ...) thanks to GraphViz_.
It handles automatic BOM (Bill of Materials) creation and has a lot of extra features.

WireViz-Web
===========
WireViz-Web wraps WireViz with a REST API using Flask. It also provides specific rendering
endpoints for PlantUML.


********
Synopsis
********
Setup::

    pip install wireviz-web

Invoke::

    # Run server.
    wireviz-web

    # Acquire WireViz YAML file.
    wget https://raw.githubusercontent.com/daq-tools/wireviz-web/main/tests/demo01.yaml

    # Render images.
    http --form http://localhost:3005/render yml_file@demo01.yaml Accept:image/svg+xml
    http --form http://localhost:3005/render yml_file@demo01.yaml Accept:image/png

    # Render HTML page with SVG image and BOM table.
    http --form http://localhost:3005/render yml_file@demo01.yaml Accept:text/html

    # Render BOM in TSV format.
    http --form http://localhost:3005/render yml_file@demo01.yaml Accept:text/plain

    # Render BOM in JSON format.
    http --form http://localhost:3005/render yml_file@demo01.yaml Accept:application/json

    # Render a PlantUML request.
    http http://localhost:3005/plantuml/svg/SyfFKj2rKt3CoKnELR1Io4ZDoSa700==
    http http://localhost:3005/plantuml/png/SyfFKj2rKt3CoKnELR1Io4ZDoSa700==

.. note::

    The ``http`` command outlined above is HTTPie_.

For visiting the Swagger OpenAPI spec, go to http://localhost:3005/doc.


*****
Tests
*****
Invoke tests, optionally with coverage report::

    poe test
    poe coverage


***********
Development
***********
As this project is still in its infancy, we humbly ask for support from the community.
Look around, give it a test drive and submit patches. There are always things to do.


.. _WireViz: https://github.com/formatc1702/WireViz
.. _WireViz fork: https://github.com/elbosso/WireViz
.. _GraphViz: https://www.graphviz.org/
.. _PlantUML: https://plantuml.com/
.. _HTTPie: https://httpie.io/

.. _Daniel Rojas: https://github.com/formatc1702
.. _Jürgen Key: https://github.com/elbosso
.. _Dyno Fu: https://github.com/dyno
.. _Rudi Yardley: https://github.com/ryardley
