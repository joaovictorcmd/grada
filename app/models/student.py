from app import db


class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    grade_1 = db.Column(db.Float, nullable=False)
    grade_2 = db.Column(db.Float, nullable=False)
    grade_3 = db.Column(db.Float, nullable=False)
    average = db.Column(db.Float, nullable=False)
    result = db.Column(db.String(10), nullable=False)  # 'Passed' or 'Failed'

    professor_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    professor = db.relationship("User", back_populates="students")

    def calculate_average(self):
        grades = [self.grade_1, self.grade_2, self.grade_3]
        self.average = round((sum(grades) / len(grades)), 1)

    def determine_result(self):
        if self.average >= 6:
            self.result = "passed"
        else:
            self.result = "failed"

    def __repr__(self):
        return f"Student: {self.first_name} {self.last_name}"
