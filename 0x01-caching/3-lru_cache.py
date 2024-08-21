#!/usr/bin/python3
"""This module contains LRUCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Represents a LRU Caching caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.order = []

    def update_order(self, key):
        """Update the order of keys based on LRU"""
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def put(self, key, item):
        """Add an item in the cache using LRU algorithm"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.order.pop(0)
            print("DISCARD:", lru_key)

            del self.cache_data[lru_key]

        self.cache_data[key] = item
        self.update_order(key)

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        self.update_order(key)
        return self.cache_data[key]
