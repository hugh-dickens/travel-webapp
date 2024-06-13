# app/__init__.py
"""
This module initializes the application.
"""

from flask import Flask

from .routes import main as main_blueprint


def create_app():
    """
    Create app
    """
    app = Flask(__name__)

    app.register_blueprint(main_blueprint)

    return app
