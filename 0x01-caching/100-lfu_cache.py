#!/usr/bin/env python3
"""Inherits BaseCaching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that implements a caching system with LFU algorithm."""

    def __init__(self):
        super().__init__()
        self.usage_frequency = {}  # Tracks frequency of usage for each key
        self.access_order = {}     # Tracks the order of access for each key
        self.counter = 0           # Incremental counter to track access order

    def put(self, key, item):
        """ Add an item in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing item and its frequency
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
        else:
            # Check if we need to evict an item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()

            # Add new item
            self.cache_data[key] = item
            self.usage_frequency[key] = 1

        # Update access order for LRU tie-breaking
        self.counter += 1
        self.access_order[key] = self.counter

    def get(self, key):
        """ Get an item by key."""
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and access order
        self.usage_frequency[key] += 1
        self.counter += 1
        self.access_order[key] = self.counter
        return self.cache_data[key]

    def evict(self):
        """ Evict the least frequently used item."""
        # Find the minimum frequency
        min_freq = min(self.usage_frequency.values())
        # Get all keys with the minimum frequency
        keys_with_min_freq = [
            key for key,
            freq in self.usage_frequency.items() if freq == min_freq]

        if len(keys_with_min_freq) > 1:
            # Use LRU to break ties
            lru_key = min(
                keys_with_min_freq,
                key=lambda k: self.access_order[k])
        else:
            lru_key = keys_with_min_freq[0]

        # Remove the selected key
        del self.cache_data[lru_key]
        del self.usage_frequency[lru_key]
        del self.access_order[lru_key]

        print(f"DISCARD: {lru_key}")
