import os
from flask import Flask, jsonify
# import datetime
from flask_sqlalchemy import SQLAlchemy
from project.api.users import users_blueprint


# Database Config
db = SQLAlchemy()


def create_app(script_info=None):

    app = Flask(__name__)

    # Set Configuration
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    # register blueprints
    app.register_blueprint(users_blueprint)
    # Shell context
    app.shell_context_processor({'app': app, 'db': db})
    return app
