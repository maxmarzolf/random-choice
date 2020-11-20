from flask import Flask, render_template, request, flash, abort
from sqlalchemy import func, desc, exc
import marko

from . import reader_bp
from app import db, models, login_manager

print('in reader_routes: ' + __name__)


@reader_bp.route("/")
def reader_home():
    raise exc.SQLAlchemyError

    try:
        posts_from_db = models.Article.get_random_articles(4)
        posts = []
        for p in posts_from_db:
            post = {"post_id": p.id, "post_title": p.title, "post_subtitle": p.subtitle, "post_date": p.posted_date}
            print(type(p.posted_date))
            post["post_content"] = p.content_html

            posts.append(post)
        
        return render_template("reader/home.html", posts=posts)
    except:
        flash('Could not retrieve posts.', 'error')
        return render_template("reader/home.html", posts=[])


@reader_bp.route("/post/<int:post_id>")
def read_post(post_id):

    post_from_db = models.Article.get_article(post_id)
    other_posts = models.Article.get_random_articles(5)

    post = {"post_id": post_from_db.id, "post_title": post_from_db.title, "post_subtitle": post_from_db.subtitle,
            "post_date": post_from_db.posted_date, "post_content": post_from_db.content_html}

    return render_template("reader/reader_view_post.html", post=post, other_posts=other_posts)
