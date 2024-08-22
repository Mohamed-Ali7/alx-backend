#!/usr/bin/python3
"""This module contains LFUCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Represents a LFU Caching caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.order = []
        self.use_frequency = {}

    def update_lru_order(self, key):
        """Update the order of keys based on LRU"""
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def put(self, key, item):
        """Add an item in the cache using LRU algorithm"""
        if key is None or item is None:
            return

        if len(self.cache_data) == self.MAX_ITEMS and key not in self.order:
            used_keys = list(self.use_frequency.keys())
            least_used = used_keys[0]
            discard_key = ''
            for k in used_keys[1:]:
                if self.use_frequency[least_used] > self.use_frequency[k]:
                    least_used = k
                    discard_key = least_used

            for k in used_keys:
                if self.use_frequency[least_used] == self.use_frequency[k]:
                    index = self.order.index(k)
                    least_used = self.order[index]
                    discard_key = self.order.pop(index)
                    break

            print("DISCARD:", discard_key)
            del self.cache_data[discard_key]
            del self.use_frequency[discard_key]

        if key in self.use_frequency:
            self.use_frequency[key] += 1
        else:
            self.use_frequency[key] = 1
        self.cache_data[key] = item
        self.update_lru_order(key)

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        if key in self.use_frequency:
            self.use_frequency[key] += 1
        self.update_lru_order(key)
        return self.cache_data[key]
