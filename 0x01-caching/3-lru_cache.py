#!/usr/bin/python3
"""This module contains LRUCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Represents a LRU Caching caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.use_frequency = {}
        self.most_recent = ''

    def put(self, key, item):
        """ Add an item in the cache"""

        if not item or not key:
            return

        keys = list(self.use_frequency.keys())

        if key in keys:
            self.most_recent = key
            self.cache_data[key] = item
            self.use_frequency[key] += 1
        elif len(self.cache_data) == self.MAX_ITEMS:
            least_used = keys[0]
            for k in keys:
                if self.use_frequency[least_used] > self.use_frequency[k]:
                    least_used = k

            del self.cache_data[least_used]
            del self.use_frequency[least_used]
            self.use_frequency[key] = self.use_frequency[self.most_recent] + 1
            self.most_recent = key
            self.cache_data[key] = item
            print("DISCARD: {}".format(least_used))
        else:
            self.most_recent = key
            self.use_frequency[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        self.most_recent = key
        return self.cache_data.get(key)
