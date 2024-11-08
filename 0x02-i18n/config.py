#!/usr/bin/env python3
"""
Configurations for my flask app
"""


class Config:
    """
    Specifies the languages available
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    TIMEZONE = "UTC"
