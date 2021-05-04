#!/usr/bin/python3
""" MRU Cache """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Class LFUCache """

    def __init__(self):
        """ Init self """
        super().__init__()
        self.ordered_cache_keys = []

    def put(self, key, item):
        """ Adds an new item in the cache """
        if not (key is None or item is None):
            if (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key not in self.cache_data.keys())
            ):
                mru = self.ordered_cache_keys[-1]
                print('DISCARD: {}'.format(mru))
                self.ordered_cache_keys.remove(mru)
                self.ordered_cache_keys.append(key)
                del self.cache_data[mru]
                self.cache_data[key] = item
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
