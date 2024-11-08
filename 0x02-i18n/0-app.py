#!/usr/bin/env python3
"""
This module sets up a basic Flask application with a single route.
The index route renders a simple HTML page that
displays 'Hello world' in the header.
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Handles the root URL and renders the index page.
    """
    return render_template('index.html')
