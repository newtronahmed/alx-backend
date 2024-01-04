#!/usr/bin/env python3
"""Task 0 module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache """

    def put(self, key, item):
        """ Assign to dictionary chache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
    
    def get(self, key):
        """ Get the item linked to key"""
        return self.cache_data.get(key, None)
