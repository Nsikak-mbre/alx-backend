#!/usr/bin/env python3
"""
Inherits from Parent class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    implements a caching system
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        assigns a value to the dictionary key
        """
        if ((key is None) or (item is None)):
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        returns dictionary value set to a key
        """
        if ((key is None) or (key not in self.cache_data)):
            return None
        return self.cache_data[key]
