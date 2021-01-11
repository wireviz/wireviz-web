*******************
WireViz-Web backlog
*******************

Iteration 1
===========
- [x] Publish on GitHub
- [x] Upload to PyPI as version 0.0.0
- [x] Notify upstream authors

Iteration 2
===========
- [x] Run black
- [x] Use version number from package
- [x] Auto-bump version on release
- [x] Add software tests
- [x] Add CI with GitHub Actions
- [x] Move to Flask-RestX, Flask-RESTPlus is no longer maintained

  - https://github.com/noirbizarre/flask-restplus/issues/770
  - https://github.com/noirbizarre/flask-restplus/pull/738
  - https://github.com/noirbizarre/flask-restplus/issues/758
  - https://github.com/noirbizarre/flask-restplus/issues/777
  - Reason: ``The import 'werkzeug.cached_property' is deprecated and will be removed in Werkzeug 1.0.``
- [x] Add parametrization to ``cli.py`` using click
- [x] Add badges to README
- [x] Adjust HTTP entrypoints
- [x] Release version 0.1.0

Iteration 3
===========
- [x] Adjust REST responses

  - 404 should respond with JSON
  - 500 should converge to 4xx
- [x] Add BOM generation endpoint
- [o] Should we add a straight ``POST`` endpoint instead of the fileupload one?
- [o] Add graphical user interface
- [o] Bring in Dockerfile again
- [o] Build and publish docker images
- [o] Cache Graphviz package on CI/GHA
  https://stackoverflow.com/questions/59269850/caching-apt-packages-in-github-actions-workflow

Iteration 4
===========
- [o] Investigate PlantUML hex vs. brotli format

    From GitLab 13.1 and later, PlantUML integration now requires a header prefix in the URL to distinguish different encoding types.

  - https://docs.gitlab.com/ee/administration/integration/plantuml.html
  - https://github.com/plantuml/plantuml/issues/117
  - https://github.com/plantuml/plantuml/pull/370
  - https://github.com/plantuml/plantuml-server/issues/152
- [o] Integrate with Kroki?
  - https://github.com/yuzutech/kroki
  - https://gitlab.com/gitlab-org/gitlab/-/issues/241744
