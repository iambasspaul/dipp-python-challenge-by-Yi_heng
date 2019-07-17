"""
App setup
"""
import os
from flask import Flask
from app.controllers.index import bp_index
from app.controllers.text import bp_text
from config.config import get_config

__all__ = ['create_app']

def create_app():
    """
    Method to create the application
    """
    app_name = 'dipp_app'
    app = Flask(app_name, instance_relative_config=True)
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(get_config(env))
    app.register_blueprint(bp_index)
    app.register_blueprint(bp_text) 
    return app
