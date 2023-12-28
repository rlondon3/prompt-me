from flask import Flask
from flask_cors import CORS
from handlers.users.users_handler import user_route
from handlers.chat_gpt.openai_handler import chat_gpt_route  
from database import connect
from init import create_app
from commands import no_db
app = create_app()

# Enable CORS for all routes
CORS(app)

@app.get("/")
def connect_db():
    return connect()

user_routes = user_route(app)
chat_gpt_routes = chat_gpt_route(app)

if __name__ == '__main__':
    app.cli.add_command(no_db)
    app.run()
