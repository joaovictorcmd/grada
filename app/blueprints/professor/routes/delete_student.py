from flask import flash, redirect, url_for
from flask_login import login_required

from .. import professor
from app.models.student import Student
from app import db


@professor.route("/delete_student/<int:student_id>", methods=["GET", "POST"])
@login_required
def delete_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)

        db.session.delete(student)
        db.session.commit()
        flash("Student successfully deleted!", category="success")
    except Exception as e:
        db.session.rollback()  # Reverte a transação para evitar inconsistências
        flash(f"An error occurred while deleting the student: {e}", category="error")

    return redirect(
        url_for("professor.home")
    )
