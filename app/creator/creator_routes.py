from flask import Flask, render_template, request

from . import creator_bp


@creator_bp.route("/creator")
def creator_home():
    return render_template("creator_home.html")


@creator_bp.route("/creator/posts/new")
def create_new_post():
    return render_template("posts/creator_new_post.html")


@creator_bp.route("/creator/posts/edit/<int:post_id>")
def creator_edit_post(post_id):
    return render_template("posts/creator_edit_post.html", post=post_id)