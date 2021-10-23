# config: utf-8

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from src.logistic import logistic as logistic_bp
    app.register_blueprint(logistic_bp)

    with app.app_context():
        db.create_all()

    return app
