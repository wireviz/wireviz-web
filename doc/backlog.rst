*******************
WireViz-Web backlog
*******************

Iteration 1
===========
- [x] Publish on GitHub
- [x] Upload to PyPI as version 0.0.0
- [o] Notify upstream authors

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
- [o] Release version 0.1.0

Iteration 3
===========
- [o] Adjust HTTP entrypoints
- [o] Adjust REST responses

  - 404 should respond with JSON
  - 500 should converge to 4xx
- [o] Add BOM generation endpoint
- [o] Add graphical user interface
- [o] Bring in Dockerfile again
- [o] Build and publish docker images
- [o] Cache Graphviz package on CI/GHA
  https://stackoverflow.com/questions/59269850/caching-apt-packages-in-github-actions-workflow
