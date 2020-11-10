from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import func

from app import db, bcrypt


# USER MODELS
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    about = db.Column(db.String(200))
    subtitle = db.Column(db.String(40))
    website = db.Column(db.String(200))
    created = db.Column(db.DateTime(), default=datetime.now)

    def create_new_password(self, form_password_plaintext):
        return bcrypt.generate_password_hash(form_password_plaintext).decode("utf-8")

    def verify_password(self, form_password):
        return bcrypt.check_password_hash(self.password, form_password)
    
    def check_passwords_match(self, form_password):
        pass

    def __repr__(self):
        return f'{self.email}'


# POST MODELS
class Article(db.Model):
    __tablename__ = 'ARTICLE'
    ID = db.Column(db.Integer(), primary_key=True)
    AUTHOR = db.Column(db.Integer(), db.ForeignKey('user.id'))
    TITLE = db.Column(db.String(length=200), nullable=False)
    SUBTITLE = db.Column(db.String(length=300), nullable=True)
    CONTENT_MARKDOWN = db.Column(db.Text(), nullable=True)
    CONTENT_HTML = db.Column(db.Text(), nullable=True)
    POSTED_DATE = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    EDITED = db.Column(db.Boolean(), nullable=False, default=False)
    ARCHIVED = db.Column(db.Boolean(), nullable=False, default=False)

    @classmethod
    def insert_article(cls, post_form):
        # should probably not presume the data is ok at this point but for now, we will
        # will need to add additional logic here later to ensure that the post object is correct

        # create the Post object from the PostForm object
        new_article = cls(TITLE=post_form.title.data, SUBTITLE=post_form.subtitle.data,
        CONTENT=post_form.content.data, POSTED_DATE=post_form.date.data, ARCHIVED=post_form.archive.data)
        
        print(new_article)        
        db.session.add(new_article)
        db.session.commit()
    
    @classmethod
    def get_article(cls, post_id):
        article = cls.query.filter_by(ID=post_id).first()

        return article
    
    @classmethod
    def get_random_articles(cls, numberOfArticles, doNotInclude=''):  
        if doNotInclude:
            articles = cls.query.filter(ID != doNotInclude).order_by(func.rand()).limit(numberOfArticles)
        else:
            articles = cls.query.order_by(func.rand()).limit(numberOfArticles)
        
        return articles

    def __repr__(self):
        return "<Post: {}>".format(self.TITLE)