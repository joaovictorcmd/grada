from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'Professor' or 'Coordinator'

    students = db.relationship("Student", back_populates="professor")

    def __repr__(self):
        return f"User: {self.email} - {self.role}"
