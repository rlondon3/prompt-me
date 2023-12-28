from flask import Flask

def create_app():
    app = Flask(__name__)

    # Other app configuration and setup code goes here

    from commands import no_db
    @app.cli.command('no_db')
    def command():
        no_db()
    return app
