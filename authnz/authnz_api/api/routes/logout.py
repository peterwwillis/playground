from flask import Blueprint

from . import bp

@bp.route('/logout')
@login_required
def AuthNZ_Logout():
    logout_user()
    return redirect(url_for("index"))

