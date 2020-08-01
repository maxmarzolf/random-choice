from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user, logout_user, login_user, login_required
from datetime import timedelta

from app import models, bcrypt, db, login_manager
from . import account_bp, account_forms

@account_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = account_forms.SignupForm()

    if request.method == "POST":
        hashed_pw = user.create_new_password(request.form["password"])

        new_user = models.User(user_email=request.form["email"], user_password=hashed_pw.decode("utf-8"))
        
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("reader_bp.reader_home"))

    return render_template("account/signup.html", form=form, current_user=current_user.__repr__())



@account_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("creator_bp.home"))
        
    form = account_forms.LoginForm()

    if form.validate_on_submit():
                
        user = models.User.query.filter_by(user_email=form.email.data).first()

        if user and user.verify_password(form.password.data):
            login_user(user, duration=timedelta(minutes=120))

            return redirect(url_for("creator_bp.home"))

    return render_template("account/login.html", form=form, current_user=current_user.__repr__())


@account_bp.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("account_bp.login"))


@account_bp.route("/account/manage", methods=["GET", "POST"])
@login_required
def manage_account():
    user_data = {"email":current_user.user_email, "password":"********", "about":current_user.user_about, "subtitle":current_user.user_subtitle, "website":current_user.user_website}

    form = account_forms.UserManagementForm(data=user_data)

    if request.method == "POST":
        updated_user = models.User.query.get(current_user.id)
        
        updated_user.user_email = current_user.user_email
        updated_user.user_password = current_user.user_password
        updated_user.user_subtitle = request.form["subtitle"]
        updated_user.user_about = request.form["about"]
        updated_user.user_website = request.form["website"]

        db.session.commit()

        return redirect(url_for("creator_bp.home"))

    return render_template("account/manage.html", form=form, current_user=current_user.__repr__())
