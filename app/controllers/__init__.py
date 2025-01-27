from flask import Blueprint, request, jsonify, make_response
from app.models.user import User

api = Blueprint('api', __name__)
data_store = []  # Pamięć RAM


# CREATE
@api.route('/api/', methods=['POST'])
def create_user():
    user_id = len(data_store) + 1
    name = request.json.get("name")
    surname = request.json.get("surname")
    email = request.json.get("email")

    if not name or not surname or not email:
        return make_response(jsonify({"error": "Missing required fields."}), 400)

    user = User(user_id, name, surname, email)
    data_store.append(user)
    response_data = {
        "success": True,
        "data": user.to_json()
    }
    return make_response(jsonify(response_data), 201)


# READ
@api.route('/api/users', methods=['GET'])
def get_users():
    response_data = {
        "success": True,
        "data": [user.to_json() for user in data_store]
    }
    return make_response(jsonify(response_data), 200)


# UPDATE
@api.route('/api/users/<int:user_id>', methods=["PUT"])
def update_user(user_id):
    if user_id < 1 or user_id > len(data_store):
        return make_response(jsonify({"error": "User not found"}), 404)

    user = data_store[user_id - 1]
    user.name = request.json.get("name", user.name)
    user.surname = request.json.get("surname", user.surname)
    user.email = request.json.get("email", user.email)

    response_data = {
        "success": True,
        "data": user.to_json()
    }
    return make_response(jsonify(response_data), 200)


# DELETE
@api.route('/api/users/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    if user_id < 1 or user_id > len(data_store):
        return make_response(jsonify({"error": "User not found"}), 404)

    data_store.pop(user_id - 1)
    response_data = {
        "success": True,
        "data": []
    }
    return make_response(jsonify(response_data), 200)
