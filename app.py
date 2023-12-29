from flask import Flask
from flask_cors import CORS
from handlers.users.users_handler import user_route
from handlers.chat_gpt.openai_handler import chat_gpt_route  
from database import connect

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

@app.get("/")
def root():
    if not app.debug:
        return connect()
    else:
        return {"message": "Database not connected"}
    
print(app.debug, 'debug')
if not app.debug:
    user_routes = user_route(app)
    chat_gpt_routes = chat_gpt_route(app)