Voici une version avec des descriptions plus brèves :

#!/usr/bin/env python3
"""
Flask app with endpoints for:
- Root URL: Welcome message
- /data: List of usernames
- /status: API status
- /users/<username>: Get user info
- /add_user: Add new user via POST
"""

from typing import Dict, Any
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# In-memory users dictionary
users: Dict[str, Dict[str, Any]] = {}

@app.route('/')
def home():
    """ Root URL: Returns welcome message """
    return Response("Welcome to the Flask API!", mimetype='text/plain')

@app.route('/data')
def get_users():
    """ Returns list of usernames in JSON """
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """ Returns API status """
    return Response("OK", mimetype='text/plain')

@app.route('/users/<username>')
def get_user(username):
    """ Retrieves user info or 404 error """
    user = users.get(username)
    return jsonify(user) if user else jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """ Adds a new user via POST request """
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    if users.get(username) == {
        "username": username, "name": data.get("name"),
        "age": data.get("age"), "city": data.get("city")
    }:
        return jsonify({"error": "User with identical details already exists"}), 400

    users[username] = {
        "username": username, "name": data.get("name"),
        "age": data.get("age"), "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

@app.errorhandler(404)
def page_not_found(e):
    """ Custom 404 error handler """
    return jsonify({"error": str(e)}), 404

if __name__ == "__main__":
    app.run()
