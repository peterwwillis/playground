
import os

from flask import Flask, render_template, redirect, request, url_for
from flask_login import (
    LoginManager,
)
from flask_wtf.csrf import CSRFProtect

from .routes import bp as routes_bp


login_manager = LoginManager()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id=user_id)

def create_app(app_name=__name__):
    app = Flask(app_name)

    #debug = os.environ.get('APP_DEBUG', False)
    #host = os.environ.get('LISTEN_ADDRESS')
    #port = int(os.environ.get('LISTEN_PORT'))

    os.environ['DEBUG']='development'
    os.environ['FLASK_DEBUG']='True'
    os.environ['TRAP_HTTP_EXCEPTIONS']='True'

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY") or os.urandom(24),
        #DEBUG=os.environ.get("FLASK_DEBUG", True),
        FLASK_DEBUG=True,
        DEBUG='development',
        TESTING=True,
        TRAP_HTTP_EXCEPTIONS=True
        # set SERVER_NAME
    )
    login_manager.init_app(app)
    app.register_blueprint(routes_bp)
    csrf.init_app(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # #OAuth 2 client setup
    # client = WebApplicationClient(GOOGLE_CLIENT_ID)

    # init_db()


    return app

