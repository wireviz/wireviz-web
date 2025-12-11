import os

import pytest

from wireviz_web import create_app
from wireviz_web.server import app as wireviz_web_app


@pytest.fixture
def app():
    app = create_app()
    app.register_blueprint(wireviz_web_app, url_prefix="")
    return app


@pytest.fixture(scope="package", autouse=True)
def reset_env():
    for key in os.environ.keys():
        if key.startswith("WIREVIZ_"):
            del os.environ[key]
