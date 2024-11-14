#!/usr/bin/env python3
""" Module of Users views
"""
import os
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Handle login of user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    if password is None or len(password) == 0:
        return jsonify({"error": "password missing"}), 400
    foundUsers = User.search({"email": email})
    if not foundUsers:
        return jsonify({"error": "no user found for this email"}), 404
    for user in foundUsers:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    user = foundUsers[0]
    GeneratedSessionID = auth.create_session(user.id)
    session_name = os.environ.get('SESSION_NAME', '_my_session_id')
    user_dict = user.to_json()
    response = make_response(jsonify(user_dict))
    response.set_cookie(session_name, GeneratedSessionID)

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Handle loginout of user
    """
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)
    if not destroy_session:
        abort(404)
    return jsonify({}), 200
