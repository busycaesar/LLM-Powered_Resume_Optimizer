from flask import Blueprint
from .data import data_api
from .generate import generate_api

api = Blueprint("api", __name__)

api.register_blueprint(data_api, url_prefix="/data")
api.register_blueprint(generate_api, url_prefix="/generate")