import sys
from flask import jsonify
from flask_login import login_required, current_user

#from app.api.errors import error_response

from . import bp
from ..basictokenauth import basic_auth, token_auth
from ..models.user import User

@bp.route('/tokens', methods=['POST'])
#@basic_auth.login_required
@login_required
def get_token():
    if current_user.is_authenticated:
        print("user is authenticated!", file=sys.stderr)
    else:
        print("user is not authenticated", file=sys.stderr)
    #token = basic_auth.current_user().get_token()
    #db.session.commit()
    token = ''
    return jsonify({'token': token})

@bp.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return '', 204

