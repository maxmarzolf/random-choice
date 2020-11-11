from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import func

from app import db, bcrypt


class User(db.Model, UserMixin):
    __tablename__ = 'USER'
    ID = db.Column(db.Integer(), primary_key=True)
    NAME = db.Column(db.String(150))
    EMAIL = db.Column(db.String(120), nullable=False)
    PASSWORD = db.Column(db.String(200), nullable=False)
    ABOUT = db.Column(db.String(100))
    PERSONAL_WEBSITE = db.Column(db.String(200))
    CREATED = db.Column(db.DateTime(), default=datetime.now)
    CLOSED = db.Column(db.Boolean(), default=False)

    @staticmethod
    def create_new_password(form_password_plaintext):
        return bcrypt.generate_password_hash(form_password_plaintext).decode("utf-8")

    @classmethod
    def verify_password(user_id, form_password):
        # update this to pass the user_id, get user password hash, and compare the form password
        # return bcrypt.check_password_hash(self.PASSWORD, form_password)
    
    @staticmethod
    def check_passwords_match(form_password):
        pass

    def __repr__(self):
        return f'{self.EMAIL} ({self.ID}, {self.NAME}, {self.CLOSED})'


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
        return f'Post: "{self.TITLE}" ({self.ID}, {self.AUTHOR}, {self.POSTED_DATE})'