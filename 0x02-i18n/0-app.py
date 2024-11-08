#!/usr/bin/env python3
"""
This module sets up a basic Flask application with a single route.
The root route renders a template displaying a welcome message.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Handles the root URL and renders the index page.

    Returns:
        str: The HTML content for the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
