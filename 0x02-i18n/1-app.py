#!/usr/bin/env python3
"""
This module sets up a basic Flask application with a single route.
The root route renders a template displaying a welcome message.
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration class for Flask app with Babel settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Handles the root URL and renders the index page.

    Returns:
        str: The HTML content for the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
