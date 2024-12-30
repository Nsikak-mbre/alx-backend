#!/usr/bin/env python3
""" Module fot pagination function """


def index_range(page: int = 1, page_size: int = 10) -> tuple:
    """
    Returns a tuple of size 2 containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for pagination parameters.

    Args:
        page (int): The current page number, defaults to 1.
        page_size (int): The number of items per page, defaults to 10.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size if page_size else 0
    end_index = page * page_size
    return (start_index, end_index)
