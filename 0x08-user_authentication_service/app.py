#!/usr/bin/env python3
""" a basic Flask """
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    """ return a JSON payload of the form """
    return jsonify({"message": "Bienvenue"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
