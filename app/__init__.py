from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hjshjhdjah kjshkjdhjs"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .blueprints.auth import auth as auth_blueprint
    from .blueprints.coordinator import coordinator as coordinator_blueprint
    from .blueprints.professor import professor as professor_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(coordinator_blueprint, url_prefix="/coordinator")
    app.register_blueprint(professor_blueprint, url_prefix="/professor")

    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    with app.app_context():
        db.create_all()

    from .models import User, Student

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("app/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
