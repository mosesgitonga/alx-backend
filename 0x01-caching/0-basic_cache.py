#!/usr/bin/env python3
"""
simple caching -> first in first out
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inheriting from BaseCaching
    """
    def put(self, key, item):
        """
        put key with item into the cache_data dictionary
        """
        if key and item:
            self.cache_data[key] = item
        else:
            return

    def get(self, key):
        """get the value of a key
        """
        if key in self.cache_data:
            value = self.cache_data.get(key)
            return value
        else:
            return None
