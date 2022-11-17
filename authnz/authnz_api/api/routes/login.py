import sys
from flask import Blueprint, render_template, flash

from . import bp
from ..forms.login import LoginForm
from ..models.user import User

@bp.route('/login', methods=["GET", "POST"])
def AuthNZ_Login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(user_id=form.user_id.data)
        if user is not None:
            if User.check_password(form.user_id.data, form.password.data) is not None:  # noqa
                login_user(user)
                flash('Logged in successfully.')
                next = request.args.get("next")
                return redirect(next or url_for("/"))
        flash("Invalid email address or Password.")
    return render_template("login.html", form=form)
    # request_uri = request.host + "/login/callback"
    # return redirect(request_uri)

