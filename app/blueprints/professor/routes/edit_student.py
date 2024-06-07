from flask import flash, redirect, request, url_for
from flask_login import current_user, login_required

from app.models.student import Student
from .. import professor
from app import db


@professor.route("/edit_student/<int:student_id>", methods=["GET", "POST"])
@login_required
def edit_student(student_id):
    if current_user.role != "professor":
        return redirect(url_for("auth.login"))

    student = Student.query.filter_by(id=student_id).first_or_404()

    if request.method == "POST":
        try:
            student.first_name = request.form.get("firstName")
            student.last_name = request.form.get("lastName")
            student.grade_1 = float(request.form.get("grade1"))
            student.grade_2 = float(request.form.get("grade2"))
            student.grade_3 = float(request.form.get("grade3"))

            student.calculate_average()
            student.determine_result()

            db.session.commit()
            flash("Student updated successfully!", category="success")
        except ValueError:
            db.session.rollback()
            flash("Please enter valid grades.", category="error")
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating student: {e}", category="error")

    return redirect(url_for("professor.home"))
