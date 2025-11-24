from apiflask import APIBlueprint

bp = APIBlueprint("home", __name__)

@bp.get("/")
def home():
    return {"message": "Hello Coupon Service"}
