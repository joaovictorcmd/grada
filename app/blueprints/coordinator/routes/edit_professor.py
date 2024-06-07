from flask import flash, redirect, request, url_for
from flask_login import login_required

from app.models.user import User
from .. import coordinator
from app import db


@coordinator.route("/edit_professor/<int:professor_id>", methods=["GET", "POST"])
@login_required
def edit_professor(professor_id):
    professor = User.query.filter_by(id=professor_id, role="professor").first_or_404()

    if request.method == "POST":
        professor.first_name = request.form.get("firstName")
        professor.last_name = request.form.get("lastName")
        professor.email = request.form.get("email")
        
        try:
            db.session.commit()
            flash("Professor updated successfully!", category="success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating professor: {e}", category="error")

    return redirect(url_for("coordinator.home"))
