#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Stockage des utilisateurs en mémoire
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


# Endpoint racine
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Endpoint pour obtenir la liste des utilisateurs
@app.route('/data', methods=['GET'])
def get_users():
    return jsonify(list(users.keys()))  # Renvoie juste les usernames


# Endpoint pour vérifier le statut de l'API
@app.route('/status', methods=['GET'])
def status():
    return "OK"


# Endpoint pour obtenir un utilisateur par son username
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# Endpoint pour ajouter un utilisateur (POST)
@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handles POST requests to add a new user.

    Expects JSON data containing 'username', 'name', 'age', and 'city'.

    Returns:
        Response: A confirmation message with the added user's data,
                or an error message if 'username' is missing or a duplicate
                with the same details exists.
    """
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    # Check if the same username with the same details exists
    existing_user = users.get(username)
    if existing_user and existing_user == {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }:
        return jsonify({
            "error": "User with identical details already exists"
        }), 400

    # If the username exists but with different details, allow it
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201  # Use 201 Created for successful POST requests

if __name__ == "__main__":
    app.run(debug=True)
