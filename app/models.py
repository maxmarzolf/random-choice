from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import func

from app import db, bcrypt


class User(db.Model, UserMixin):
    __tablename__ = 'USER'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    about = db.Column(db.String(100))
    personal_website = db.Column(db.String(200))
    created = db.Column(db.DateTime(), default=datetime.now)
    closed = db.Column(db.Boolean(), default=False)

    @classmethod
    def get_user_by_id(cls, user_id):
        user = cls.query.filter_by(id=user_id).first()
        return user

    @classmethod
    def get_user_by_email(cls, user_email):
        user = cls.query.filter_by(email=user_email).first()
        return user

    @classmethod
    def update_user(cls, user):
        # id, about, name, personal_website
        #_id, *_data = user.items() # this is less secure, potentially, because it allows some other values to be snuck into the tuple
        _user_data = {"about": user["about"], "name": user["name"], "personal_website": user["personal_website"]}
        cls.query.filter_by(id=user["id"]).update(_user_data)
        db.session.commit()
        #return true

    @classmethod
    def create_new_user(cls, user_email, user_password_plaintext):
        new_user = cls(email=user_email, password=cls._create_new_password(user_password_plaintext))

        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def _create_new_password(password_plaintext):
        return bcrypt.generate_password_hash(password_plaintext).decode("utf-8")

    @classmethod
    def verify_password(cls, user_id, form_password):
        # update this to pass the user_id, get user password hash, and compare the form password
        # return bcrypt.check_password_hash(self.PASSWORD, form_password)
        user = cls.query.filter_by(id=user_id).first()
        return bcrypt.check_password_hash(user.password, form_password)
    
    @staticmethod
    def check_passwords_match(form_password):        
        pass

    def __repr__(self):
        return f'{self.email} ({self.id}, {self.name}, {self.closed})'


class Article(db.Model):
    __tablename__ = 'ARTICLE'
    id = db.Column(db.Integer(), primary_key=True)
    author = db.Column(db.Integer(), db.ForeignKey('USER.id'))
    title = db.Column(db.String(length=200), nullable=False)
    subtitle = db.Column(db.String(length=300), nullable=True)
    content_markdown = db.Column(db.Text(), nullable=True)
    content_html = db.Column(db.Text(), nullable=True)
    posted_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    edited = db.Column(db.Boolean(), nullable=False, default=False)
    archived = db.Column(db.Boolean(), nullable=False, default=False)

    @classmethod
    def insert_article(cls, post_form):
        # create the Post object from the PostForm object
        new_article = cls(title=post_form.title.data, subtitle=post_form.subtitle.data,
        content=post_form.content.data, posted_date=post_form.date.data, archived=post_form.archive.data)
        
        db.session.add(new_article)
        db.session.commit()
    
    @classmethod
    def get_article(cls, post_id):
        article = cls.query.filter_by(id=post_id).first()

        return article
    
    @classmethod
    def get_random_articles(cls, numberOfArticles, doNotInclude=''):  
        if doNotInclude:
            articles = cls.query.filter(id != doNotInclude).order_by(func.random()).limit(numberOfArticles)
        else:
            articles = cls.query.order_by(func.random()).limit(numberOfArticles)
        
        return articles

    def __repr__(self):
        return f'Post: "{self.title}" ({self.id}, {self.author}, {self.posted_date})'