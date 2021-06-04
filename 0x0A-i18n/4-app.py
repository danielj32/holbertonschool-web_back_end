#!/usr/bin/env python3
""" Flask app
basic components """
from flask import Flask, app, render_template, g, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ class for
    Basic Babel setup"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('1-app.Config')


@app.route('/')
def helloWorld():
    """return render
    index template """
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """ determine the
    best match with
    our supported languages """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
