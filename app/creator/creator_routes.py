from flask import render_template, request
from flask_login import login_required

from . import creator_bp, creator_forms
from app import models


@creator_bp.route("/me")
@login_required
def home():
    return render_template("creator/creator_home.html")


@creator_bp.route("/me/posts/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = creator_forms.PostForm()
    if request.method == "POST":
        models.Article.insert_post(form)
    return render_template("creator/creator_new_post.html", form=form)


@creator_bp.route("/me/posts/edit/<int:post_id>")
@login_required
def edit_post(post_id):
    return render_template("creator/creator_edit_post.html", post=post_id)

