from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ, path
from dotenv import load_dotenv

basedirectory = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedirectory, '.env'))

SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = environ.get("SECRET_KEY")

# import models
from app.models import User, Post, db

# create an engine
eng = create_engine(SQLALCHEMY_DATABASE_URI)

# bind the SQLAlchemy instance to the engine
db.metadata.bind = eng

db.metadata.create_all()

DBSession = sessionmaker(bind=eng)
session = DBSession()

# posts
users = [
    User(email='company@comp.any', password='$2b$12$E4Vmrz/GoZ3hU2nIS4LiUezjT3jsqXnMBjwutFbRgMH/vEoo2sAZq', about='About Me!', subtitle='App Developer',
                website='website.web', first_name='John', last_name='Doe'),        
    User(email='email@email.com', password='$2b$12$E4Vmrz/GoZ3hU2nIS4LiUezjT3jsqXnMBjwutFbRgMH/vEoo2sAZq', about='Its me, Mario.', subtitle='Sr. DB Admin',
                website='mypage.github.com', first_name='Mario', last_name='Plumbed'),
    User(email='send@grid.net', password='$2b$12$E4Vmrz/GoZ3hU2nIS4LiUezjT3jsqXnMBjwutFbRgMH/vEoo2sAZq', about='Info about me.', subtitle='Unemployed',
                website='mysite.web', first_name='Michael', last_name='Bretts'),
    User(email='jdoe@outlook.com', password='', about='Python. Flask. SQL.', subtitle='Aspiring full stack engineer', first_name='Jane', last_name='Doe')
]

for u in users:
    session.add(u)


# posts
posts = [
    Post(
        post_title='Post Title 1',
        post_subtitle='Post Subtitle 1',
        post_content='# Post content',
        post_was_edited=False,
        post_archived=False
    ),
    Post(
        post_title='Post Title 2',
        post_subtitle='Post 2 Subtitle',
        post_content='# Post 2 Content \n## Post 2 subheader',
        post_was_edited=True,
        post_archived=True
    ),
    Post(
        post_title='Post Title 3',
        post_subtitle='Post 3 Subtitle',
        post_content=("# Post 3 Section Header\n"
        "## Post 3 Section Subheader\n"
        "+ first item\n"
        "+ second item\n"
        "+ third item\n\n" # blank line separates the list from the paragraph
        "And some paragraph text.")
    )
]

for p in posts:
    session.add(p)

session.commit()
session.close()
