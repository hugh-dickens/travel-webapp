# app/__init__.py

from flask import Flask
from flask_cors import CORS  # Import CORS
from app.routes import main as main_blueprint

def create_app():
    app = Flask(__name__)
    
    # Enable CORS for all origins on all routes
    CORS(app)

    # Register blueprints and other configurations
    app.register_blueprint(main_blueprint)

    return app

