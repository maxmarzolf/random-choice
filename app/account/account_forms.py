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
    email = EmailField("Email")
    password = PasswordField("Password")
    about = TextAreaField("About", validators=[Length(max=200), Optional()])
    subtitle = StringField("Subtitle", validators=[Length(max=40), Optional()])
    website = StringField("Website", validators=[Length(max=200), Optional()])