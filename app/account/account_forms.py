from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, Optional, Email

class SignupForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired(), Email(message="Valid email required.")])
    password = PasswordField("Password", validators=[InputRequired()])


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired(), Email(message="Valid email required.")])
    password = PasswordField("Password", validators=[InputRequired()])


class UserManagementForm(FlaskForm):
    name = StringField("Name", validators=[Length(max=150), Optional()])
    about = TextAreaField("About", validators=[Length(max=200), Optional()])
    website = StringField("Website", validators=[Length(max=200), Optional()])


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old Password")
    new_password = PasswordField("New Password")