from wireviz_web import create_app
from wireviz_web.server import wireviz_blueprint


def run():

    # Create Flask application.
    app = create_app()

    # Register WireViz-Web component.
    # TODO: Parametrize URL prefix.
    app.register_blueprint(wireviz_blueprint, url_prefix="")

    # Invoke Flask application.
    # TODO: Parametrize listen address and debug mode.
    app.run(host='127.0.0.1', port=3005, debug=True)
