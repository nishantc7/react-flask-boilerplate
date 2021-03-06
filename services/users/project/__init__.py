import os
from flask import Flask
# import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


# Instantiate Config
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(script_info=None):

    app = Flask(__name__)

    # Enable CORS
    CORS(app)

    # Set Configuration
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # register blueprints
    # Import must be here to avoid circular import issue
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    from project.api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    # Shell context
    app.shell_context_processor({'app': app, 'db': db})
    return app
