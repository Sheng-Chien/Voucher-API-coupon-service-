# app/views/__init__.py
from apiflask import APIFlask
from .coupons import bp as coupons_bp   # 這裡才是 .coupons
from .home import bp as home_bp

def register_blueprints(app: APIFlask):
    app.register_blueprint(home_bp)
    app.register_blueprint(coupons_bp)
