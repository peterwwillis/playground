from flask_login import (
    LoginManager,
    # current_user,
    login_required,
    login_user,
    logout_user,
)

# import forms
# forms import LoginForm
#from forms import LoginForm
#from user import User


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


#def application(env, start_response):
#    return app

#def main():
#    app.run(os.environ["LISTEN_ADDRESS"], os.environ["LISTEN_PORT"], debug)

#if __name__ == "__main__":
#    main()