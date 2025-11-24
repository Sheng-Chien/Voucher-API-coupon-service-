# app/views/coupons.py
from apiflask import APIBlueprint

bp = APIBlueprint("coupons", __name__, url_prefix="/coupons")

@bp.get("/")
def list_coupons():
    return {"items": []}
