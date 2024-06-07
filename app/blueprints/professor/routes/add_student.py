from flask import flash, redirect, request, url_for
from flask_login import current_user, login_required

from app.models.student import Student
from .. import professor
from app import db


@professor.route("/add_student", methods=["GET", "POST"])
@login_required
def add_student():
    if current_user.role != "professor":
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        try:
            first_name = request.form.get("firstName")
            last_name = request.form.get("lastName")
            grade_1 = float(request.form.get("grade1"))
            grade_2 = float(request.form.get("grade2"))
            grade_3 = float(request.form.get("grade3"))

            # Validate grades
            if not all(0 <= grade <= 10 for grade in [grade_1, grade_2, grade_3]):
                raise ValueError("Grades must be between 0 and 10.")

            new_student = Student(
                first_name=first_name,
                last_name=last_name,
                grade_1=grade_1,
                grade_2=grade_2,
                grade_3=grade_3,
                professor_id=current_user.id
            )
            new_student.calculate_average()
            new_student.determine_result()

            db.session.add(new_student)
            db.session.commit()
            flash("Student added successfully!", category="success")
        except ValueError:
            db.session.rollback()
            flash("Please enter valid grades.", category="error")
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding student: {e}", category="error")

    return redirect(url_for("professor.home"))
