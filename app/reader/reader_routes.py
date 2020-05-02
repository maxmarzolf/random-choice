from flask import Flask, render_template, request

from . import reader_bp
from app import db, models


@reader_bp.route("/")
def reader_home():
    return "reader home!"


@reader_bp.route("/post/<int:post_id>")
def read_post(post_id):
    post = models.Post._get_post(post_id)
    print(post)

    return render_template("reader_view_post.html", post=post)