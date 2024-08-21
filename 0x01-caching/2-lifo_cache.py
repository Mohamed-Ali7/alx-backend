#!/usr/bin/python3
"""This module contains LIFOCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Represents a FIFO caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache"""

        if not item or not key:
            return

        if len(self.cache_data) == self.MAX_ITEMS and key not in self.keys:
            del self.cache_data[self.keys[-1]]
            print("DISCARD: {}".format(self.keys.pop()))

        self.keys.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""

        return self.cache_data.get(key)
