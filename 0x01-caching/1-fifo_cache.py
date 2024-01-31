#!/usr/bin/env python3
"""
simple cache
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key and item:
            if len(self.cache_data) >=  BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print('DISCARD: {}'.format(first_key))
            self.cache_data[key] = item

    def get(self, key, value):
        if key in self.cache_data:
            value = self.cache_data.get(key)
            return value
        return None