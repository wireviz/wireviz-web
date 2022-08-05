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
.. image:: https://pepy.tech/badge/wireviz-web/month
    :target: https://pepy.tech/project/wireviz-web

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
For compatibility with PlantUML_, it includes a `PlantUML Text Encoding format`_
decoder by `Dyno Fu`_ and `Rudi Yardley`_.

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


*****
Setup
*****

Install prerequisites::

    {apt,brew,dnf,yum,zypper} install python3 graphviz

Install package::

    pip install wireviz-web


*****
Usage
*****

Run server::

    wireviz-web

Invoke requests::

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

    The ``http`` command used in the examples is the excellent HTTPie_ program.

For visiting the Swagger OpenAPI spec, go to http://localhost:3005/doc.



*******************
Project information
*******************

Contributions
=============

Every kind of contribution, feedback, or patch, is much welcome. `Create an
issue`_ or submit a patch if you think we should include a new feature, or to
report or fix a bug.

Development
===========

In order to setup a development environment on your workstation, please head
over to the `development sandbox`_ documentation. When you see the software
tests succeed, you should be ready to start hacking.

Resources
=========

- `Source code repository <https://github.com/daq-tools/wireviz-web>`_
- `Documentation <https://github.com/daq-tools/wireviz-web/blob/main/README.rst>`_
- `Python Package Index (PyPI) <https://pypi.org/project/wireviz-web/>`_

License
=======

The project is licensed under the terms of the GNU AGPL license.


.. _create an issue: https://github.com/daq-tools/wireviz-web/issues
.. _Daniel Rojas: https://github.com/formatc1702
.. _development sandbox: https://github.com/daq-tools/wireviz-web/blob/main/doc/sandbox.rst
.. _Dyno Fu: https://github.com/dyno
.. _GraphViz: https://www.graphviz.org/
.. _HTTPie: https://httpie.io/
.. _Jürgen Key: https://github.com/elbosso
.. _PlantUML: https://plantuml.com/
.. _PlantUML Text Encoding format: https://plantuml.com/text-encoding
.. _Poetry: https://pypi.org/project/poetry/
.. _Rudi Yardley: https://github.com/ryardley
.. _WireViz: https://github.com/formatc1702/WireViz
.. _WireViz fork: https://github.com/elbosso/WireViz
