from flask import Blueprint, request, jsonify
from app.services.service import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError

user_bp = Blueprint('user_routes', __name__)

@user_bp.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    try:
        return create_user(data)
    except NotUniqueError:
        return jsonify({"error": "Email already exists"}), 409
    except (KeyError, ValidationError) as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route('/users', methods=['GET'])
def read_all():
    return jsonify(get_all_users()[0]), 200

@user_bp.route('/users/<user_id>', methods=['GET'])
def read_one(user_id):
    try:
        return jsonify(get_user_by_id(user_id)[0]), 200
    except DoesNotExist:
        return jsonify({"error": "User not found"}), 404

@user_bp.route('/users/<user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    try:
        return update_user(user_id, data)
    except DoesNotExist:
        return jsonify({"error": "User not found"}), 404
    except NotUniqueError:
        return jsonify({"error": "Email already exists"}), 409

@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete(user_id):
    try:
        return delete_user(user_id)
    except DoesNotExist:
        return jsonify({"error": "User not found"}), 404
