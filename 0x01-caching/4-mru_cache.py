#!/usr/bin/env python3
""" Task 4 module"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implementation of MRUCache"""

    def __init__(self):
        """Iniitialize cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item to cache"""
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", first_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Get item """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
