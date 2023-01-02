
import sys

from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user

from . import bp
from ..forms.login import LoginForm
from ..models.user import User

@bp.route('/login', methods=["GET", "POST"])
def AuthNZ_Login():
    form = LoginForm()
    import pprint
    #pprint.pprint(request.form, stream=sys.stderr)
    #pprint.pprint(vars(form), stream=sys.stderr)
    #tkn='csrf_token'
    #if tkn in form:
    #    print("csrf_token '%s'" % form.tkn, file=sys.stderr)
    if form.validate_on_submit():
        user = User.get(user_id=form.user_id.data)
        print("got user '%s'" % user, file=sys.stderr)
        if user is not None:
            if User.check_password(form.user_id.data, form.password.data) is not None:  # noqa
                print("login_user(user)", file=sys.stderr)
                login_user(user)
                flash('Logged in successfully.')
                next = request.args.get("next")
                return redirect(next or url_for("routes.AuthNZ_Home"))
        flash("Invalid email address or Password.")
    return render_template("login.html", form=form)
    # request_uri = request.host + "/login/callback"
    # return redirect(request_uri)

