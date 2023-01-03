
import os
import sys

from flask import Flask #, render_template, redirect, request, url_for
from flask_login import (
    LoginManager,
)
from flask_wtf.csrf import CSRFProtect

from .routes import bp as routes_bp
from .models.user import User


login_manager = LoginManager()
csrf = CSRFProtect()


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401

@login_manager.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    token = request.args.get('token')
    if token:
        printf("found token '%s'" % token, file=sys.stderr)
        user = User.query.filter_by(token=token).first()
        printf("found user '%s'" % user, file=sys.stderr)
        if user:
            return user

    # next, try to login using Basic Auth
    token = request.headers.get('Authorization')
    if token:
        printf("found token '%s'" % token, file=sys.stderr)
        token = token.replace('Basic ', '', 1)
        try:
            token = base64.b64decode(token)
        except TypeError:
            pass
        user = User.query.filter_by(token=token).first()
        printf("found user '%s'" % user, file=sys.stderr)
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None

@login_manager.user_loader
def load_user(user_id):
    print("load_user()", file=sys.stderr)
    return User.get(user_id=user_id)

def create_app(app_name=__name__):
    app = Flask(app_name)

    #debug = os.environ.get('APP_DEBUG', False)
    #host = os.environ.get('LISTEN_ADDRESS')
    #port = int(os.environ.get('LISTEN_PORT'))

    #os.environ['DEBUG']='development'
    os.environ['FLASK_DEBUG']='True'
    os.environ['TRAP_HTTP_EXCEPTIONS']='True'

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY") or os.urandom(24),
        #DEBUG=os.environ.get("FLASK_DEBUG", True),
        FLASK_DEBUG=True,
        #DEBUG='development',
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

