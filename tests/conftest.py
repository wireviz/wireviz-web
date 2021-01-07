import pytest

from wireviz_web import create_app
from wireviz_web.server import wireviz_blueprint


@pytest.fixture
def app():
    app = create_app()
    app.register_blueprint(wireviz_blueprint, url_prefix="")
    return app
