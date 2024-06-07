from flask import Blueprint

# Create the Blueprint for authentication
auth = Blueprint("auth", __name__, template_folder="templates")

# Import all routes from the routes directory
from .routes import login, sign_up, logout
