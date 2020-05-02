from app import db


# USER MODELS


# POST MODELS
class Post(db.Model):
    post_id = db.Column(db.Integer(), primary_key=True)
    author_id = db.Column(db.Integer())
    post_title = db.Column(db.String(length=200))
    post_subtitle = db.Column(db.String(length=300))
    post_content = db.Column(db.Text())
    post_date = db.Column(db.DateTime())
    post_was_edited = db.Column(db.Boolean())
    post_archived = db.Column(db.Boolean())

    @classmethod
    def insert_post(cls, post_form):
        # should probably not presume the data is ok at this point but for now, we will
        # will need to add additional logic here later to ensure that the post object is correct

        # create the Post object from the PostForm object
        new_post = cls(post_title=post_form.title.data, post_subtitle=post_form.subtitle.data,
        post_content=post_form.content.data, post_date=post_form.date.data, post_archived=post_form.archive.data)

        print(new_post)        
        db.session.add(new_post)
        db.session.commit()
    
    @staticmethod
    def _get_post(post_id):
        post = Post.query.filter_by(post_id=post_id).first()

        return post
        

    def __repr__(self):
        return "<Post: {}>".format(self.post_title)