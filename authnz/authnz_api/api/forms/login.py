
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired(), Length(min=4, max=25)]
    )
    #email = StringField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me", validators=[])
    submit = SubmitField("Login")
