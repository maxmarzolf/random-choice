from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import func
import markdown

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
        _user_data = {"about": user["about"], "name": user["name"], "personal_website": user["personal_website"]}
        cls.query.filter_by(id=user["id"]).update(_user_data)
        db.session.commit()

    @classmethod
    def update_password(cls, user_id, old_password, new_password):
        user = cls.query.filter_by(id=user_id).first()
        if bcrypt.check_password_hash(user.password, old_password):
            cls.query.filter_by(id=user_id).update({"password": cls._create_new_password(new_password)})
            db.session.commit()

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
        user = cls.query.filter_by(id=user_id).first()
        return bcrypt.check_password_hash(user.password, form_password)

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
    def insert_article(cls, post_form, user_id):
        new_article = cls(title=post_form.title.data, subtitle=post_form.subtitle.data,
                          content_markdown=post_form.content.data, content_html=markdown.markdown(post_form.content.data),
                          author=user_id, posted_date=post_form.date.data, archived=post_form.archive.data)

        db.session.add(new_article)
        db.session.commit()
    
    @classmethod
    def update_article(cls, article_id, article_form):
        print(article_form)        
        article = {"title": article_form.title.data, "subtitle": article_form.subtitle.data, "content_markdown": article_form.content.data, 
                    "content_html":markdown.markdown(article_form.content.data), "archived": article_form.archive.data, "edited": True}
        cls.query.filter_by(id=article_id).update(article)
        db.session.commit()

    @classmethod
    def get_article(cls, post_id):
        article = cls.query.filter_by(id=post_id).first()

        return article
    
    @classmethod
    def get_articles_by_author(cls, author_id):
        articles = cls.query.filter_by(author=author_id).all()

        return articles

    @classmethod
    def get_all_articles(cls):
        articles = cls.query.order_by(Article.posted_date.desc())
        return articles

    @classmethod
    def get_random_articles(cls, number_of_articles, do_not_include=''):
        if do_not_include:
            articles = cls.query.filter(id != do_not_include).order_by(func.random()).limit(number_of_articles)
        else:
            articles = cls.query.order_by(func.random()).limit(number_of_articles)

        return articles

    def __repr__(self):
        return f'Post: "{self.title}" ({self.id}, {self.author}, {self.posted_date})'
