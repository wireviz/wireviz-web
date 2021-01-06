from flask import Flask


def create_app(test_config=None) -> Flask:
    """
    Create and configure the Flask application, with CORS.

    - https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
    - https://flask-cors.readthedocs.io/

    :param test_config:
    :return: Configured Flask application.
    """

    # Create Flask application.
    app = Flask(__name__)

    # Initialize Cross Origin Resource sharing support for
    # the application on all routes, for all origins and methods.
    # CORS(app)
    # app.config['CORS_HEADERS'] = 'Content-Type'

    return app
