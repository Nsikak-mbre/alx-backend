#!/usr/bin/env python3
"""
Returns a tuple of size 2
"""


def index_range(page: int = 1, page_size: int = None) -> tuple:
    start_index = (page - 1) * page_size if page_size else 0
    end_index = page * page_size if page_size else 0
    return (start_index, end_index)
