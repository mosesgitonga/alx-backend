#!/usr/bin/python3
"""
simple caching -> first in first out
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """inheriting from BaseCaching
    """
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item
        else:
            return
        
    def get(self, key):
        if key in self.cache_data:
            value = self.cache_data.get(key)
            return value
        else:
            return None
