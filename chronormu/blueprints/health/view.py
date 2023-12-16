from flask import Blueprint

health = Blueprint("health", __name__)


@health.get("/")
def index():
    return {"status": "alive"}
