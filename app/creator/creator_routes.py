from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import current_user, logout_user, login_user, login_required

from . import creator_bp, creator_forms
from app import models, bcrypt, db, login_manager


@creator_bp.route("/creator")
@login_required
def home():
    return render_template("creator/creator_home.html")


@creator_bp.route("/creator/posts/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = creator_forms.PostForm()

    if request.method == "POST":
        models.Post.insert_post(form)

    return render_template("creator/creator_new_post.html", form=form)


@creator_bp.route("/creator/posts/edit/<int:post_id>")
@login_required
def edit_post(post_id):
    return render_template("creator/creator_edit_post.html", post=post_id)

