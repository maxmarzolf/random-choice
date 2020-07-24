from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.ext.dateutil.fields import DateTimeField
from wtforms.validators import InputRequired, Length, Optional, Email


class PostForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(min=4, max=200)])
    subtitle = StringField("Subtitle", validators=[Optional(), Length(max=300)])
    content = TextAreaField("Content", validators=[InputRequired()], render_kw={"rows": "10"})
    date = DateTimeField("Post Date/Time", display_format="%Y/%M/%D --- %HH:%MM:%ss", validators=[InputRequired()])
    archive = BooleanField("Archive")

# does there need to be 2 separate forms for a form? can auto-populate be toggled?
# create post form

class SignupForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired(), Email(message="Valid email required.")])
    password = PasswordField("Password", validators=[InputRequired()])