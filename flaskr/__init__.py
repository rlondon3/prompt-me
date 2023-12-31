from flask import Flask
from flask_cors import CORS
from flaskr.handlers.users.users_handler import user_route
from flaskr.handlers.chat_gpt.openai_handler import chat_gpt_route
from flaskr.database import connect


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Enable CORS for all routes
    CORS(app)

    @app.route("/")
    def root():
        return connect()

    # Register user routes
    user_route(app)

    # Register chat GPT routes
    chat_gpt_route(app)

    return app
