#!/usr/bin/env python3
"""
Inherits from Base class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements a FIFO caching policy
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        determines which resource is stored in cache
        """
        if ((key is None) or (item is None)):
            return
        self.cache_data[key] = item
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            first_key = list(self.cache_data.keys())[0]
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        returns dictionary value set to a key
        """
        if ((key is None) or (key not in self.cache_data)):
            return None
        return self.cache_data[key]
