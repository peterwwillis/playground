
import sys

from flask_httpauth import HTTPTokenAuth
# from app.api.errors import error_response

#from . import bp
from .models.user import User

token_auth = HTTPTokenAuth(scheme='Bearer')

@token_auth.verify_token
def verify_token(token):
    if token:
        return User.check_token(token)
    return None

@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)

