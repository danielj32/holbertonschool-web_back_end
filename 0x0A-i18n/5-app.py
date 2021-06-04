#!/usr/bin/env python3
""" Flask app
basic components """
from flask import Flask, app, render_template, g, request
from flask_babel import Babel, _
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ class for
    Basic Babel setup"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('1-app.Config')
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def helloWorld():
    """return render
    index template """
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """ determine the
    best match with
    our supported languages """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """ determine if a
    user is logged in, and the language """
    id = request.args.get('login_as')
    d_user = get_user(id)
    if d_user:
        g.user = d_user


def get_user(id):
    """ returns a user
    dictionary or None """
    if id and int(id) in users:
        return users[int(id)]
    return None


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
