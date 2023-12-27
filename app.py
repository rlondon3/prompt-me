from flask import Flask
from flask_cors import CORS
from handlers.users.users_handler import user_route
from handlers.chat_gpt.openai_handler import chat_gpt_route  
from database import connect

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.get("/")
def connect_db():
    return connect()

user_routes = user_route(app)
chat_gpt_routes = chat_gpt_route(app)
