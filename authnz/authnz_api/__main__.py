# import json
import os

from flask import (
    Flask, 
    render_template, 
    flash, 
    redirect, 
    request, 
    url_for
)
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    UserMixin
)
from forms import LoginForm
from user import User


app = Flask(__name__)
app.config.from_mappping(
    SECRET_KEY=os.environ.get("SECRET_KEY") or os.urandom(24),
)

login_manager = LoginManager()
login_manager.init_app(app)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# #OAuth 2 client setup
# client = WebApplicationClient(GOOGLE_CLIENT_ID)


debug = False
if "DEBUG" in os.environ and os.environ["DEBUG"]:
    debug = True


# Flask-Login helper to retrieve a user
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
def index():
    return render_template('index.html')
    #if current_user.is_authenticated:
    #else:
    #    return '<a class="button" href="/login">Login</a>'


@app.route("/login", methods=["GET", "POST"])
def AuthNZ_Login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(form.username.data)
        if user is not None and user.check_password(form.password.data) is not None:
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('/'))
        flash('Invalid email address or Password.')    
    return render_template('login.html', form=form)
    #request_uri = request.host + "/login/callback"
    #return redirect(request_uri)


@app.route("/logout")
@login_required
def AuthNZ_Logout():
    logout_user()
    return redirect(url_for("index"))


def flask_get_arg(name):
    if name in request.form:
        # print("got form item '%s'='%s'" % (name,value), file=sys.stderr)
        return request.form[name]
    else:
        # print("got arg item '%s'='%s'" % (name,value), file=sys.stderr)
        return request.args.get(name)


def flask_get_content(name):
    if name in request.files:
        contentf = request.files[name]
        if contentf.filename == "":
            flash("No selected file")
            return redirect(request.url)
        # print("got form content '%s'" % (name))
        return contentf.read()
    else:
        # print("got arg content '%s'" % name)
        return request.args.get(name)


def main():
    app.run(os.environ["FLASK_ADDRESS"], os.environ["FLASK_PORT"], debug)


if __name__ == "__main__":
    main()
