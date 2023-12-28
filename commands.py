# commands.py
import subprocess
from flask import current_app
from database import disconnect

def run_flask_app():
    """Run the Flask app in a separate process."""
    disconnect()
    subprocess.run(["flask", "run", "--debug"], check=True)

def no_db():
    """Run the app without connecting to the database."""
    disconnect()
    # Run the Flask app in a separate process to avoid blocking the CLI command
    run_flask_app()
