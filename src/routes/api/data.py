from flask import Blueprint, request, jsonify
from routes.response import response

data_api = Blueprint("data_api", __name__)

@data_api.route("/job-description", methods=["POST"])
def post_job_description():
    # Takes the document link from the request body.
    # Takes the job description from the document link.
    # Generates the summarized version of the job description, retaining the key skills, essentional keywords and important information about the company.
    # Stores the summarized version in the database and sends a positive response.
    return jsonify(response(True, "Job description is stored.")), 201

@data_api.route("/master-data", methods=["POST"])
def post_master_data():
    # Takes the document link from the request body.
    # Takes the master data from the document link.
    # Creates the embeddings of the master data.
    # Stores the embeddings and the master data in the vector database and sends a positive response.
    return jsonify(response(True, "Master data is stored.")), 201

@data_api.route("/resume", methods=["POST"])
def post_resume():
    # Takes the document link from the request body.
    # Stores the document link in the database and sends a positive response.
    return jsonify(response(True, "Resume document link is stored.")), 201