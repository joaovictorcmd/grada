from flask import Blueprint

# Create the Blueprint for coordinator
coordinator = Blueprint('coordinator', __name__, template_folder='templates')

# Import all routes from the routes directory
from .routes import home, edit_professor, delete_professor
