from flask import Flask, render_template, request
from sqlalchemy import func, desc

from . import reader_bp
from app import db, models


@reader_bp.route("/")
def reader_home():
    posts = models.Post.query.order_by(desc(models.Post.post_date)).limit(4)
    return render_template("home.html", posts=posts)


@reader_bp.route("/post/<int:post_id>")
def read_post(post_id):
    post = models.Post._get_post(post_id)
    other_posts = models.Post.query.filter(models.Post.post_id != post.post_id).order_by(func.random()).limit(5)
    
    print(other_posts)
    print(post)

    return render_template("reader_view_post.html", post=post, other_posts=other_posts)