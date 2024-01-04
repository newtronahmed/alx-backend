#!/usr/bin/env python3
"""Task 0 module"""
class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")

class BasicCache(BaseCaching):
    """ Basic Cache """

    def put(self, key, item):
        """ Assign to dictionary chache"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})
    
    def get(self, key):
        """ Get the item linked to key"""
        if key is not None:
            return self.cache_data.get(key)
        else:
            return key
