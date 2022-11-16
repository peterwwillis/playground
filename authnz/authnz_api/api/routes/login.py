import sys
from flask import Blueprint, render_template, flash

from . import bp
from ..forms.login import LoginForm
from ..models.user import User

@bp.route('/login', methods=["GET", "POST"])
def AuthNZ_Login():
    print("woooo! login!", file=sys.stderr)
    form = LoginForm()
    print("validating", file=sys.stderr)
    if form.validate_on_submit():
        u = User(
            user_id=form.username.data
        )
        user = u.get()
        print("got user obj", file=sys.stderr)
        # fmt: off
        if user is not None and user.check_password(form.password.data) is not None:  # noqa
            # fmt: on

            login_user(user)
            flash('Logged in successfully.')

            next = request.args.get("next")
            return redirect(next or url_for("/"))
        flash("Invalid email address or Password.")
    return render_template("login.html", form=form)
    # request_uri = request.host + "/login/callback"
    # return redirect(request_uri)

