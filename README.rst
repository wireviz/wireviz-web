###########
WireViz-Web
###########


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
WireViz is a tool for easily documenting cables, wiring harnesses and connector pinouts.
It takes plain text, YAML-formatted files as input and produces beautiful graphical output
(SVG, PNG, ...) thanks to GraphViz_.
It handles automatic BOM (Bill of Materials) creation and has a lot of extra features.


********
Synopsis
********
::

    # Render a plain YAML file.
    echo "Bob -> Alice : hello" > test.yml
    http --form http://127.0.0.1:3005/render yml_file@test.yml Accept:image/svg+xml
    http --form http://127.0.0.1:3005/render yml_file@test.yml Accept:image/png

    # Render a PlantUML request.
    http http://127.0.0.1:3005/svg/SyfFKj2rKt3CoKnELR1Io4ZDoSa700==
    http http://127.0.0.1:3005/png/SyfFKj2rKt3CoKnELR1Io4ZDoSa700==


***********
Development
***********
As this is still in its infancy, we humbly ask for support from the community.
Look around, give it a test drive and submit patches.


.. _WireViz: https://github.com/formatc1702/WireViz
.. _WireViz fork: https://github.com/elbosso/WireViz
.. _Daniel Rojas: https://github.com/formatc1702
.. _Jürgen Key: https://github.com/elbosso
.. _GraphViz: https://www.graphviz.org/
.. _PlantUML: https://plantuml.com/
.. _Dyno Fu: https://github.com/dyno
.. _Rudi Yardley: https://github.com/ryardley
