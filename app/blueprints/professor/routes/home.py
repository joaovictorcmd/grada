from flask import redirect, render_template, url_for
from flask_login import current_user, login_required

from app.models.student import Student
from .. import professor


@professor.route("/")
@login_required
def home():
    if current_user.role != "professor":
        return redirect(url_for("auth.login"))

    students = Student.query.all()
    return render_template("professor.html", user=current_user, students=students)
