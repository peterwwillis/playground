
from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user

from . import bp

@bp.route('/logout', methods=["POST"])
@login_required
def AuthNZ_Logout():
    logout_user()
    return redirect(url_for("routes.AuthNZ_Home"))

