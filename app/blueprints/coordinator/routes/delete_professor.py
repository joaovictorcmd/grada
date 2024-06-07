from flask import flash, redirect, url_for
from flask_login import login_required

from app.models.user import User
from .. import coordinator
from app import db


@coordinator.route("/delete_professor/<int:professor_id>", methods=["GET", "POST"])
@login_required
def delete_professor(professor_id):
    try:
        professor = User.query.get_or_404(professor_id)

        if professor.role != "professor":
            flash("You do not have permission to delete this user.", category="error")
        else:
            db.session.delete(professor)
            db.session.commit()
            flash("Professor deleted successfully!", category="success")
    except Exception as e:
        db.session.rollback()
        flash(f"An error occurred while deleting the professor: {e}", category="error")

    return redirect(
        url_for("coordinator.home")
    )
