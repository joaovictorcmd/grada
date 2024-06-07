from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

from .. import auth
from app.models.user import User


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash("Logged in successfully!", category="success")

                if user.role == "coordinator":
                    return redirect(url_for("coordinator.home"))
                elif user.role == "professor":
                    return redirect(url_for("professor.home"))
                else:
                    flash("Role not recognized.", "error")
                    return redirect(url_for("auth.login"))

            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login.html", user=current_user)
