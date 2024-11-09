#!/usr/bin/env python3
"""
This module sets up a basic Flask application with a single route.
The root route renders a template displaying a welcome message.
"""

from flask_babel import Babel, gettext as _
from flask import Flask, render_template, request, g


class Config:
    """Configuration class for Flask app with Babel settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages based on the
    Accept-Language header in the request or the 'locale' query parameter.

    Returns:
        str: The best match language code, such as 'en' or 'fr'.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> dict:
    """
    Retrieves a user dictionary based on the 'login_as' query parameter.

    Returns:
        dict: The user dictionary if found, otherwise None.
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    Executed before all other functions. Sets the user as a global variable if found.
    """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """
    Handles the root URL and renders the index page.

    Returns:
        str: The HTML content for the index page.
    """
    return render_template('5-index.html', home_title=_('home_title'), home_header=_('home_header'))


if __name__ == '__main__':
    app.run()
