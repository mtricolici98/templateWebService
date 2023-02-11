from flask import Blueprint, jsonify, request

example_blueprint = Blueprint('example', import_name=__name__)


@example_blueprint.route('/example')
def example_get_endpoint():
    return jsonify("Success"), 200


@example_blueprint.route('/example/post', methods=["POST"])
def example_post_endpoint():
    data = request.json()
    return jsonify("Success"), 200
