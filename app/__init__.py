# app/__init__.py
from apiflask import APIFlask

from config import Config
from .extensions import init_db
from .views import register_blueprints   # ✅ 從 views 匯入

def create_app() -> APIFlask:
    app = APIFlask(__name__, title="Coupon Service", version="1.0.0")
    app.config.from_object(Config)

    # 初始化資料庫
    init_db(app)

    # 註冊所有藍圖
    register_blueprints(app)

    return app
