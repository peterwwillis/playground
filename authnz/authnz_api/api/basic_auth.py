import sys
from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPTokenAuth
# from app.api.errors import error_response

#from . import bp
from .models.user import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme='Bearer')

@basic_auth.verify_password
def verify_password(user_id, password):
    user = User.get(user_id=user_id)
    if user and user.check_password(password):
        return user

@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)

@token_auth.verify_token
def verify_token(token):
    if token:
        return User.check_token(token)
    return None

@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)

