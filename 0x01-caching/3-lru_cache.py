#!/usr/bin/env python3
"""Task 0 module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Implementation of lru cache"""

    def __init__(self):
        """Initialize clas"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ PUt an item in cache"""
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cach_data.popitems(True)
                print("DISCARED:", last_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """ Get item from cache"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
