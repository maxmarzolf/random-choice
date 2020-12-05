from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
#from wtforms.ext.dateutil.fields import DateTimeField
from wtforms.fields.html5 import DateTimeField
from wtforms.validators import InputRequired, Length, Optional


class PostForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(min=4, max=200)])
    subtitle = StringField("Subtitle", validators=[Optional(), Length(max=300)])
    content = TextAreaField("Content", validators=[InputRequired()], render_kw={"rows": "10"})
    date = DateTimeField("Post Date/Time", validators=[InputRequired()])
    archive = BooleanField("Archive")
