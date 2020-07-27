from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import current_user, logout_user, login_user, login_required

from . import creator_bp, creator_forms
from app import models, bcrypt, db, login_manager


@creator_bp.route("/creator")
@login_required
def creator_home():
    return render_template("creator/creator_home.html")


@creator_bp.route("/creator/posts/new", methods=["GET", "POST"])
@login_required
def create_new_post():
    form = creator_forms.PostForm()

    if request.method == "POST":
        print(request.form)
        print(type(form.date.data))
        models.Post.insert_post(form)

    return render_template("creator/creator_new_post.html", form=form)


@creator_bp.route("/creator/posts/edit/<int:post_id>")
@login_required
def creator_edit_post(post_id):
    return render_template("creator/creator_edit_post.html", post=post_id)


@creator_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = creator_forms.SignupForm()

    if request.method == "POST":
        hashed_pw = bcrypt.generate_password_hash(request.form["password"])

        new_user = models.User(user_email=request.form["email"], user_password=hashed_pw.decode("utf-8"))
        
        db.session.add(new_user)
        db.session.commit()

    return render_template("login/signup.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return models.User.query.get(user_id)
    
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash("You must log in to view this page.")

    return redirect(url_for('creator_bp.login'))


@creator_bp.route("/login", methods=["GET", "POST"])
def login():
    form = creator_forms.LoginForm()

    if request.method == "POST":
        if current_user.is_authenticated:
            return redirect(url_for("creator_bp.creator_home"))
        
        if form.validate_on_submit():
            user = models.User.query.filter_by(user_email=form.email.data).first()

            if user and bcrypt.check_password_hash(user.user_password, form.password.data):
                login_user(user)

        return render_template("creator/creator_home.html")

    return render_template("login/login.html", form=form)

@creator_bp.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("creator_bp.login"))