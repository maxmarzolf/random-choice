from flask import Flask, render_template, request

from . import creator_bp, creator_forms
from app import models


@creator_bp.route("/creator")
def creator_home():
    return render_template("creator/creator_home.html")


@creator_bp.route("/creator/posts/new", methods=["GET", "POST"])
def create_new_post():
    form = creator_forms.PostForm()

    if request.method == "POST":
        print(request.form)
        print(type(form.date.data))
        models.Post.insert_post(form)

    return render_template("creator/creator_new_post.html", form=form)


@creator_bp.route("/creator/posts/edit/<int:post_id>")
def creator_edit_post(post_id):
    return render_template("creator/creator_edit_post.html", post=post_id)