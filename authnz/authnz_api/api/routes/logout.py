from flask import Blueprint
from flask_login import login_required

from . import bp

@bp.route('/logout')
@login_required
def AuthNZ_Logout():
    logout_user()
    return redirect(url_for("index"))

