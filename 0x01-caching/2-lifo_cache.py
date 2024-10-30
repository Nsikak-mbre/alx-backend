#!/usr/bin/env python3
"""
Inherits from Base class
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    Implements a LIFO caching policy
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        determines which resource is stored in cache
        """
        if key is None or item is None:
            return
        # Remove the key if it already exists to maintain LIFO order
        if key in self.cache_data:
            del self.cache_data[key]

        # locate and delete the last received item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_key}")

        # Now add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """
        returns dictionary value set to a key
        """
        if ((key is None) or (key not in self.cache_data)):
            return None
        return self.cache_data[key]
