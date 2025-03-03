from flask import Blueprint, request, jsonify
from routes.response import response

generate_api = Blueprint("generate_api", __name__)

@generate_api.route("/skills", methods=["POST"])
def post_skills():
    # Takes the stored job description.
    # Gets the content of the resume using the stored document link.
    # Adds the job description and resume content into the prompt template.
    # Sends the prompt template to the LLM to generate the response.
    # Returns a positive response along with the generated response.
    return jsonify(response(True, "Suggested skills are sent.")), 200

@generate_api.route("/projects", methods=["POST"])
def post_projects():
    # Takes the stored job description.
    # Gets the relevant master data content chunk from the vector database.
    # Adds the job description and relevant content chunk into the prompt template.
    # Sends the prompt template to the LLM to generate the response.
    # Returns a positive response along with the generated response.
    return jsonify(response(True, "Suggested projects along with updated description are sent.")), 200

@generate_api.route("/summary", methods=["POST"])
def post_summary():
    # Takes the stored job description.
    # Gets the content of the resume using the stored document link.
    # Adds the job description and resume content into the prompt template.
    # Sends the prompt template to the LLM to generate the response.
    # Returns a positive response along with the generated response.
    return jsonify(response(True, "Suggested summary is sent.")), 200

@generate_api.route("/ats-check", methods=["POST"])
def post_ats_check():
    # Takes the stored job description.
    # Gets the content of the resume using the stored document link.
    # Adds the job description and resume content into the prompt template.
    # Sends the prompt template to the LLM to generate the response.
    # Returns a positive response along with the generated response.
    return jsonify(response(True, "Resume's ATS score and suggests the updates for increasing the score is sent.")), 200