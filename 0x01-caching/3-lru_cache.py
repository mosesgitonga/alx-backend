#!/usr/bin/env python3
"""
last recently used
"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """
    caching -> last recently used 
    """
    def __init__(self):
        super().__init__()
        self.order_of_keys = []

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the least recently used item (the first item in the order_of_keys list)
                lru_key = self.order_of_keys.pop(0)
                del self.cache_data[lru_key]
                print('DISCARD:', lru_key)
            self.cache_data[key] = item
            self.order_of_keys.append(key)


    def get(self, key):
        if key is not None:
            if key in self.cache_data:
                self.order_of_keys.remove(key)
                self.order_of_keys.append(key)
                return self.cache_data[key]
        return None
