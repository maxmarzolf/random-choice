from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.ext.dateutil.fields import DateTimeField
from wtforms.validators import InputRequired, Length, Optional


class PostForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(min=4, max=200)])
    subtitle = StringField("Subtitle", validators=[Optional(), Length(max=300)])
    content = StringField("Content", validators=[InputRequired()])
    date = DateTimeField("Post Date/Time", display_format="%Y/%M/%D --- %HH:%MM:%ss", validators=[InputRequired()])
    archive = BooleanField("Archive")

# does there need to be 2 separate forms for a form? can auto-populate be toggled?
# create post form
