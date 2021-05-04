#!/usr/bin/python3
""" BasicCache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching
        and is a caching system """
    def put(self, key, item):
        """ Adding new item """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Getting and new item """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
