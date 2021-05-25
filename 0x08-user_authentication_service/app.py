#!/usr/bin/env python3
""" a basic Flask """
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """ return a JSON payload of the form """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """ registers a
    new users """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=['POST'])
def sessions():
    """new session for the user,store it
    the session ID as a cookie
    with key "reference_id" on the response
    and return a JSON payload """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    reference_id = AUTH.create_session(email)
    if not reference_id:
        abort(401)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("reference_id", reference_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ user logout by destroying the session_id """
    cookie = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(cookie)
    if user is None:
        abort(403)
    else:
        AUTH.destroy_session(user.id)
        return redirect('/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
