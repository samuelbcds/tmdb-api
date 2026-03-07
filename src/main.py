import os
from flask import Flask, jsonify, request
from src.config.config import config
from src.routes.route import api


def create_app(config_name=None):
    
    app = Flask(__name__)
    
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app.config.from_object(config.get(config_name, config['default']))
    
    app.register_blueprint(api)

    return app