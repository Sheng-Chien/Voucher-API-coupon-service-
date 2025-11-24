from flask_sqlalchemy import SQLAlchemy

# 使用 SQLAlchemy 2.0 style
db = SQLAlchemy()


def init_db(app):
    db.init_app(app)

