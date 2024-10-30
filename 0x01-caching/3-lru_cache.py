#!/usr/bin/env python3
"""
Inherits from Base class
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Implements a LRU caching policy
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

        # Remove the key if it already exists to maintain the order
        if key in self.cache_data:
            del self.cache_data[key]

        # If the cache exceeds its max limit, remove the least recently used
        # item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        # add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """
        returns dictionary value set to a key
        """
        if ((key is None) or (key not in self.cache_data)):
            return None

        # Move the accessed key to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
