#!/usr/bin/env python3
"""
Basic Flask app setup.
"""

from flask import Flask, render_template
from typing import Any

app = Flask(__name__)


@app.route('/')
def index() -> Any:
    """Renders the index page."""
    return render_template('index.html')

