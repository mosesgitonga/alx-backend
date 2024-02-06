#!/usr/bin/env python3
"""
Basic babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel
from tzlocal import get_localzone


app = Flask(__name__)

babel = Babel(app)


class Config():
    """
    configuration for babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def welcome():
    """
    welcome page route
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
