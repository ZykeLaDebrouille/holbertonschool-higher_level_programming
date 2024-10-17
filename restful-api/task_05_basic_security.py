Voici le code avec les descriptions résumées :

#!/usr/bin/env python3
"""
Ce script configure une application Flask avec authentification basique et JWT,
y compris le contrôle d'accès basé sur les rôles.

Usage :
- Exécutez le script et utilisez un client HTTP comme curl ou Postman pour interagir avec l'API.
"""

from functools import wraps
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Clé secrète pour JWT (à remplacer par une clé sécurisée en production)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

# Données utilisateur en mémoire
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Vérifie les identifiants utilisateur."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return True
    return False


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Route protégée par authentification basique."""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Renvoie un token JWT si les identifiants sont valides."""
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password required"}), 400

    username = data['username']
    password = data['password']
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(
            identity={'username': username, 'role': user['role']}
        )
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Route protégée nécessitant un JWT valide."""
    return "JWT Auth: Access Granted"


def admin_required(fn):
    """Vérifie que l'utilisateur a le rôle d'administrateur."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        jwt_identity = get_jwt_identity()
        if jwt_identity and jwt_identity.get('role') == 'admin':
            return fn(*args, **kwargs)
        else:
            return jsonify({"error": "Admin access required"}), 403
    return wrapper


@app.route('/admin-only')
@jwt_required()
@admin_required
def admin_only():
    """Route accessible uniquement aux administrateurs."""
    return "Admin Access: Granted"


# Gestionnaires d'erreurs pour JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(_err):
    """Gère les erreurs JWT non autorisées."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(_err):
    """Gère les erreurs de token JWT invalide."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(_jwt_header, _jwt_payload):
    """Gère les erreurs de token expiré."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(_jwt_header, _jwt_payload):
    """Gère les erreurs requérant un token frais."""
    return jsonify({"error": "Fresh token required"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(_jwt_header, _jwt_payload):
    """Gère les erreurs de token révoqué."""
    return jsonify({"error": "Token has been revoked"}), 401


if __name__ == "__main__":
    app.run()
