#!/usr/bin/env python3
""" Module fot pagination function """

import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        "returns a representation of a requested resource as specified"
        assert isinstance(
            page, int) and isinstance(
            page_size, int), "Both page and page_size must be integers."
        assert page > 0 and page_size > 0, "Both page and page_size must"
        "be greater than 0."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
