from flask import Blueprint, request, jsonify
from routes.response import response

generate_api = Blueprint("generate_api", __name__)

@generate_api.route("/skills", methods=["POST"])
def post_skills():
    # Takes the document link from the request body.
    # Stores the document link in the database and sends a positive response.
    return jsonify(response(True, "Resume document link is stored.")), 200