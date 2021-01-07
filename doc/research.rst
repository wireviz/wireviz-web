############################
WireViz integration research
############################

Standing on the shoulders of giants.


WireViz GUI and Service
=======================
Within those discussions, `Daniel Rojas`_, Jason_, `Jürgen Key`_
and `Tyler Ward`_ are talking about the baseline work needed
to bring the functionality of WireViz into a graphical user
interface and a service.

- https://github.com/formatc1702/WireViz/pull/55
- https://github.com/formatc1702/WireViz/pull/68
- https://github.com/slightlynybbled/wireviz-gui

.. _Daniel Rojas: https://github.com/formatc1702
.. _Jason: https://github.com/slightlynybbled
.. _Jürgen Key: https://github.com/elbosso
.. _Tyler Ward: https://github.com/Tyler-Ward


Integration of TeX and WireViz into GitLab through PlantUML
===========================================================
`Jürgen Key`_ says:

    GitLab_ already provides integration for PlantUML_ diagrams.
    I added two more: Wiring looms and harnesses can be easily
    and beautifully visualized with WireViz - I integrated this too.
    And - naturally - TeX formulas are a must...

- https://elbosso.github.io/wireviz_docker_container.html
- https://www.youtube.com/watch?v=gB1UfRYJoYc

This is how it works:

- https://github.com/elbosso/plantumlinterfaceproxy#wireviz
- https://github.com/elbosso/plantumlinterfaceproxy#configuration
- https://github.com/elbosso/plantumlinterfaceproxy/blob/1.1.0/app/server.py#L199-L203
- https://github.com/elbosso/WireViz/blob/master/src/app/server.py

.. _GitLab: https://gitlab.com/
.. _PlantUML: https://plantuml.com/


Integration of WireViz into Discourse
=====================================
`Andreas Motl`_ says:

    I just had a quick look. `discourse-graphviz`_ uses `Viz.js`_ for layout and
    rendering [1,2], so it stays exclusively in the browser scope.
    However, it also shells out to ImageMagick_ to render a PNG [3].

    So, both techniques are represented (JS context evaluation as well as classic shellout).
    With the latter, one could possibly also create a ``WireViz`` variant.

.. _Andreas Motl: https://github.com/amotl
.. _discourse-graphviz: https://github.com/discourse/discourse-graphviz
.. _Viz.js: https://github.com/mdaines/viz.js
.. _ImageMagick: https://www.imagemagick.org/


| [1] https://github.com/discourse/discourse-graphviz/blob/4173abc/plugin.rb#L17
| [2] https://github.com/discourse/discourse-graphviz/blob/4173abc/plugin.rb#L35
| [3] https://github.com/discourse/discourse-graphviz/blob/4173abc/plugin.rb#L62
