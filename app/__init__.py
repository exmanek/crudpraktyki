from flask import Flask
from app.controllers import api

def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False
    app.register_blueprint(api)
    return app