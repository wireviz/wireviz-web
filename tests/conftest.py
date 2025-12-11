import pytest

from wireviz_web import create_app
from wireviz_web.server import app as wireviz_web_app


@pytest.fixture
def app():
    app = create_app()
    app.register_blueprint(wireviz_web_app, url_prefix="")
    return app
