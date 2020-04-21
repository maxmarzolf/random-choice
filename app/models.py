from app import db


# USER MODELS


# POST MODELS
class Post(db.Model):
    post_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    post_title = db.Column(db.String(length=200))
    post_subtitle = db.Column(db.String(length=300))
    post_content = db.Column(db.Text())
    post_date = db.Column(db.DateTime())
    post_was_edited = db.Column(db.Boolean())
    post_archived = db.Column(db.Boolean())