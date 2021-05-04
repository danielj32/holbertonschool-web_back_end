#!/usr/bin/python3
""" LRU cache """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Class LRUCache  """

    def __init__(self):
        """ Init self """
        super().__init__()
        self.ordered_cache_keys = []

    def put(self, key, item):
        """ Adds an  new item in the cache """
        if not (key is None or item is None):
            if (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key not in self.cache_data.keys())
            ):
                lru = self.ordered_cache_keys[0]
                print('DISCARD: {}'.format(lru))
                self.ordered_cache_keys.pop(0)
                del self.cache_data[lru]
                self.cache_data[key] = item
                self.ordered_cache_keys.append(key)
            elif (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key in self.cache_data.keys())
            ):
                self.ordered_cache_keys.remove(key)
                self.ordered_cache_keys.append(key)
                self.cache_data[key] = item
            else:
                self.ordered_cache_keys.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """ Gets an  new item by key """
        if key not in self.cache_data.keys():
            return None
        else:
            self.ordered_cache_keys.remove(key)
            self.ordered_cache_keys.append(key)
            return self.cache_data[key]
