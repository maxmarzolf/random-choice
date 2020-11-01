from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ, path
from dotenv import load_dotenv
from datetime import timedelta

basedirectory = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedirectory, '.env'))

SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = environ.get("SECRET_KEY")


# import models
from app.models import User, Post, db

# create an engine
eng = create_engine(SQLALCHEMY_DATABASE_URI)
print(type(db))
print(type(db.Model))
print(db.metadata.schema)

db.metadata.bind = eng
db.metadata.create_all()

# there aren't multiple datasources so this bind is unnecessary. It will default to SQLALCHEMY_DATABASE_URI.
# print(db.metadata)
# print(dir(db.metadata))
# db.metadata.bind = eng
# print(db.metadata)

# create the sessionmaker
DBSession = sessionmaker(bind=eng)

# create a session
session = DBSession()

# define new objects for INSERT
new_user1 = User(email='company@comp.any', password='$2b$12$E4Vmrz/GoZ3hU2nIS4LiUezjT3jsqXnMBjwutFbRgMH/vEoo2sAZq', about='About Me!', subtitle='App Developer',
            website='website.web', first_name='John', last_name='Doe')
        
new_user2 = User(email='email@email.com', password='$2b$12$E4Vmrz/GoZ3hU2nIS4LiUezjT3jsqXnMBjwutFbRgMH/vEoo2sAZq', about='Its me, Mario.', subtitle='Sr. DB Admin',
            website='mypage.github.com', first_name='Mario', last_name='Plumbed')

new_user3 = User(email='send@grid.net', password='$2b$12$E4Vmrz/GoZ3hU2nIS4LiUezjT3jsqXnMBjwutFbRgMH/vEoo2sAZq', about='Info about me.', subtitle='Unemployed',
            website='mysite.web', first_name='Michael', last_name='Bretts')

# session.add + session.commit
session.add(new_user1)
session.add(new_user2)
session.add(new_user3)
session.commit()
session.close()
