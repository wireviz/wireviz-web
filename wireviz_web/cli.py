import click

from wireviz_web import create_app
from wireviz_web.server import wireviz_blueprint
from wireviz_web.util import setup_logging


@click.command(
    help="""A wrapper around WireViz for bringing it to the web. 
    Easily document cables and wiring harnesses."""
)
@click.option(
    "--listen",
    type=str,
    required=False,
    default="localhost:3005",
    help="The address the server should listen on." "Defaults to: localhost:3005",
)
@click.option(
    "--url",
    type=str,
    required=False,
    default="",
    help="On wich URL prefix to respond." "Defaults to: /",
)
@click.option(
    "--debug",
    is_flag=True,
    required=False,
    default=False,
    help="Whether to run the server in debug mode",
)
def run(listen: str, url: str, debug: bool):

    # Setup logging.
    setup_logging()

    # Create Flask application.
    app = create_app()

    # Register WireViz-Web component.
    app.register_blueprint(wireviz_blueprint, url_prefix=url)

    # Invoke Flask application.
    host, port = listen.split(":")
    app.run(host=host, port=int(port), debug=debug)
