"""WireViz-Web - a wrapper around WireViz for bringing it to the web. Easily document cables and wiring harnesses."""
__appname__ = "wireviz-web"


# Single-sourcing the package version
# https://cjolowicz.github.io/posts/hypermodern-python-06-ci-cd/
try:
    from importlib.metadata import PackageNotFoundError, version  # noqa
except ImportError:  # pragma: no cover
    from importlib_metadata import PackageNotFoundError, version  # noqa

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

import logging
import os

from flask import Flask
from flask_cors import CORS

logger = logging.getLogger(__name__)


def create_app(test_config=None) -> Flask:
    """
    Create and configure the Flask application, with CORS.

    - https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
    - https://flask-cors.readthedocs.io/

    :param test_config:
    :return: Configured Flask application.
    """

    logger.info("Init " + __appname__)
    # Create Flask application.
    app = Flask(__name__)

    # Initialize Cross Origin Resource sharing support for
    # the application on all routes, for all origins and methods.
    # enable cors if flag is set
    if os.getenv("CORS_ENABLE", "False").lower() in ("true", "1", "t"):
        CORS(app)
        # app.config['CORS_HEADERS'] = 'Content-Type'
        logger.info("CORS enabled for all routes")

    return app
