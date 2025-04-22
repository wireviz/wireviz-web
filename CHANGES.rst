*********************
WireViz-Web changelog
*********************


in progress
===========

- Add support for Python 3.12
- Remove support for Python 3.7
- Updated to WireViz 0.4.1


2023-01-18 0.4.1
================

- Add support for Python 3.11
- Update to flask-restx 1.0.5


2022-09-19 0.4.0
================

- Add Dockerfile support to repository. Thanks, @Jacq.
- Add CORS support via ``CORS_ENABLE`` environment variable. Thanks, @Jacq.


2022-08-05 0.3.2
================
- Update dependencies and project tooling
- Drop support for Python 3.6


2021-11-09 0.3.1
================
- Upgrade to WireViz 0.3.1
- WireViz 0.3.1 makes ``wireviz.parse()``'s ``file_out`` argument optional again.


2021-10-22 0.3.0
================
- CI: Run test suite on Python 3.10
- CI: Upgrade ``setup-poetry`` action. Add version pinning for Poetry 1.1.11
- Upgrade foundation libraries Flask, Flask-RESTX and Click
- Upgrade to WireViz 0.3. Thanks, @formatc1702!


2021-01-11 0.2.0
================
- Add rendering for HTML (SVG and BOM), TEXT (BOM) and JSON (BOM)


2021-01-10 0.1.0
================
- Use version number from ``wireviz_web.__version__``
- Add software tests
- Add CI with GitHub Actions
- Use ``flask-restx`` instead of ``flask-restplus``
- Parametrize ``wireviz_web.cli``
- Run coverage testing on CI, with Codecov
- Generalize API/core routines
- Adjust error response texts
- Respond with JSON body on 404 errors
- Improve inline documentation
- Run Black and isort
- Move PlantUML API endpoint to /plantuml prefix


2021-01-06 0.0.0
================
- Initial import
