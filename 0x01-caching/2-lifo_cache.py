#!/usr/bin/env python3
"""
caching last in first out
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    last in first out
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        put key with value
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print('DISCARD: {}'.format(last_key))
            self.cache_data[key] = item

    def get(self, key):
        """get value
        """
        return self.cache_data.get(key, None)