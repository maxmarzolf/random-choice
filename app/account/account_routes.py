from flask import request, redirect, url_for, render_template, flash, session
from flask_login import current_user, logout_user, login_user, login_required, fresh_login_required
from datetime import timedelta
from urllib.parse import urlparse, urljoin
#from is_safe_url import is_safe_url

from app import models, bcrypt, db, login_manager
from . import account_bp, account_forms

def is_safe_url(target_url):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target_url))
    return test_url.scheme in ("http", "https") and ref_url.netloc == test_url.netloc

@account_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = account_forms.SignupForm()

    if request.method == "POST":
        # proper try/except here.
        models.User.create_new_user(form.email.data, form.password.data)

        return redirect(url_for("reader_bp.reader_home"))

    return render_template("account/signup.html", form=form, current_user=current_user.__repr__())



@account_bp.route("/login", methods=["GET", "POST"])
def login():       
    form = account_forms.LoginForm()

    if form.validate_on_submit():
        # if current_user.is_authenticated:
        #     return redirect(url_for("creator_bp.home"))
                
        user = models.User.get_user_by_email(form.email.data)

        if user and user.verify_password(user.id, form.password.data):
            login_user(user, duration=timedelta(minutes=1), remember=True)
            print(session)

            if "next" in session:
                next_url = session["next"]
                session.pop("next")
                session.modified = True
                print("next in session")
                print(session)
                if is_safe_url(next_url):
                    print("url is safe")
                    return redirect(next_url)
                else:
                    print("url is not safe")
                    return redirect(url_for("creator_bp.home"))
            else:
                print("next is not in session")
                return redirect(url_for("creator_bp.home"))
        else:
            flash("Please enter a valid user name and password.")

    return render_template("account/login.html", form=form, current_user=current_user.__repr__())


@account_bp.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("account_bp.login"))


@account_bp.route("/me/manage", methods=["GET", "POST"])
@login_required
def manage_account():
    user_data = {"about":current_user.about, "website":current_user.personal_website, "name":current_user.name}
    print(session)
    form = account_forms.UserManagementForm(data=user_data)

    if request.method == "POST":
        updated_user = {"id": current_user.id, "about": form.about.data, "name": form.name.data, "personal_website": form.website.data}

        models.User.update_user(updated_user)

        return redirect(url_for("creator_bp.home"))

    return render_template("account/manage.html", form=form, current_user=current_user.__repr__())


@account_bp.route("/me/password", methods=["GET", "POST"])
@fresh_login_required
def change_password():
    form = account_forms.ChangePasswordForm()

    if form.validate_on_submit():
        models.User.update_password(user_id=current_user.id, old_password=form.old_password.data, new_password=form.new_password.data)

        return redirect(url_for("creator_bp.home"))


    return render_template("account/change_password.html", form=form)


