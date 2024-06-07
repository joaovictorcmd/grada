from flask import render_template
from flask_login import current_user, login_required

from app.models.user import User
from .. import coordinator


@coordinator.route("/")
@login_required
def home():
    professors = User.query.filter_by(role="professor").all()

    return render_template("coordinator.html", user=current_user, professors=professors)
