#!/usr/bin/python3
"""This module contains BasicCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Represents a caching system"""

    def put(self, key, item):
        """ Add an item in the cache"""

        if not item or not key:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""

        return self.cache_data.get(key)
