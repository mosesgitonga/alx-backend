#!/usr/bin/env python3
"""
Basic babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel
from tzlocal import get_localzone


app = Flask(__name__)


class Config():
    """
    configuration for babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def welcome():
    """
    welcome page route
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)