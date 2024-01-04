#!/usr/bin/env python3
"""Task 1 module"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ first in first out cache implementation"""
    
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item to cache"""
        if key is None and item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_value = self.cache_data.popitem(false)
            self.cache_data[key] = item
            print("DISCARD: {}".(first_value))

    def get(self, key):
        """ Get item linked to cache key"""
        return self.cache_data.get(key, None)
