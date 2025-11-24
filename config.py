import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 可以改成 PostgreSQL 等資料庫
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(BASE_DIR, 'coupon.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    # APIFlask 設定
    TITLE = "Coupon Service"
    VERSION = "1.0.0"
    DESCRIPTION = "Simple coupon management API for interview demo"


config = Config()
