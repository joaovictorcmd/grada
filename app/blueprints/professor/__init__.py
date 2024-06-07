from flask import Blueprint

# Create the Blueprint for professor
professor = Blueprint('professor', __name__, template_folder='templates')

# Import all routes from the routes directory
from .routes import home, add_student, edit_student, delete_student
