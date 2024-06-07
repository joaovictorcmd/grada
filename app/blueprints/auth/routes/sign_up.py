from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from .. import auth
from app.models.user import User


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        role = request.form.get("role")
        first_name = request.form.get("firstName")
        last_name = request.form.get("lastName")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists.", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif len(last_name) < 2:
            flash("Last name must be greater than 1 character.", category="error")
        elif password != confirm_password:
            flash("Passwords don't match.", category="error")
        elif len(password) < 7:
            flash("Password must be at least 7 characters.", category="error")
        else:
            new_user = User(
                role=role,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=generate_password_hash(
                    password, method="pbkdf2:sha256", salt_length=8
                ),
            )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success")

            if new_user.role == "coordinator":
                return redirect(url_for("coordinator.home"))
            elif new_user.role == "professor":
                return redirect(url_for("professor.home"))

    return render_template("sign-up.html", user=current_user)
