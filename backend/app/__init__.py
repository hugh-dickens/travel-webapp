# app/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from app.models import db
from app.routes import main as main_blueprint


# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Enable CORS for all origins on all routes
    CORS(app)

    # Database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # Initialize Migrate with the app and db instance
    migrate = Migrate(app, db)

    # Register blueprints and other configurations
    app.register_blueprint(main_blueprint)

    return app
