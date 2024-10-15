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
    user_data = request.get_json()
    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = user_data
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
