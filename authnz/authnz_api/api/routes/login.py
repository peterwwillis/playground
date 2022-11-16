from flask import Blueprint

from . import bp

@bp.route('/login', methods=["GET", "POST"])
def AuthNZ_Login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(form.username.data)
        # fmt: off
        if user is not None and user.check_password(form.password.data) is not None:  # noqa
            # fmt: on
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for("/"))
        flash("Invalid email address or Password.")
    return render_template("login.html", form=form)
    # request_uri = request.host + "/login/callback"
    # return redirect(request_uri)

