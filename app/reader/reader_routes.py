from flask import Flask, render_template, request
from sqlalchemy import func, desc
import marko

from . import reader_bp
from app import db, models, login_manager


@reader_bp.route("/")
def reader_home():
    # posts_from_db = models.Post.query.order_by(desc(models.Post.post_date)).limit(4)
    #
    # posts = []
    # for p in posts_from_db:
    #     post = {}
    #     post["post_id"] = p.post_id
    #     post["post_title"] = p.post_title
    #     post["post_subtitle"] = p.post_subtitle
    #     post["post_date"] = p.post_date
    #     post["post_content"] = marko.convert(p.post_content)
    #
    #     posts.append(post)
    #
    return render_template("reader/home.html")


@reader_bp.route("/post/<int:post_id>")
def read_post(post_id):
    post_from_db = models.Post._get_post(post_id)
    other_posts = models.Post.query.filter(models.Post.post_id != post_from_db.post_id).order_by(func.random()).limit(5)

    post = {}
    post["post_id"] = post_from_db.post_id
    post["post_title"] = post_from_db.post_title
    post["post_subtitle"] = post_from_db.post_subtitle
    post["post_date"] = post_from_db.post_date
    post["post_content"] = marko.convert(post_from_db.post_content)

    return render_template("reader/reader_view_post.html", post=post, other_posts=other_posts)
