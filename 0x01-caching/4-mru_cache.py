#!/usr/bin/env python3
"""
MRUCache module that inherits from BaseCaching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    Implements a MRU caching policy
    """

    def __init__(self):
        """Initialize the class with OrderedDict"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache using LRU policy
        """
        if key is None or item is None:
            return

        # If key already exists, delete it to maintain order
        if key in self.cache_data:
            del self.cache_data[key]
        
        # If cache is full, pop the first (least recently used) item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {mru_key}")

         # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key and mark it as recently used
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
