#!/usr/bin/env python3
"""
This module sets up a basic Flask application with a single route.
The root route renders a template displaying a welcome message.
"""

from flask_babel import Babel, _
from flask import Flask, render_template, request


class Config:
    """Configuration class for Flask app with Babel settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages based on the
    Accept-Language header in the request.

    Returns:
        str: The best match language code, such as 'en' or 'fr'.
    """
    # Check if 'locale' query parameter is present and valid
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Handles the root URL and renders the index page.

    Returns:
        str: The HTML content for the index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
