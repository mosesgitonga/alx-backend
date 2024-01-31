#!/usr/bin/env python3
"""
caching of most rcently used
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    most recently used
    """
    def __init__(self):
        super().__init__()
        self.order_of_keys = []

    def put(self, key, item):
        """
        put into dict
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the most recently used item (the last item in the order_of_keys list)
                mru_key = self.order_of_keys.pop()
                del self.cache_data[mru_key]
                print('DISCARD:', mru_key)
            
            # Add the new item to the cache and update the order_of_keys list
            self.cache_data[key] = item
            self.order_of_keys.append(key)

    def get(self, key):
        """
        get value from dict
        """
        if key is not None:
            if key in self.cache_data:
                # Move the accessed key to the end to mark it as most recently used
                self.order_of_keys.remove(key)
                self.order_of_keys.append(key)
                return self.cache_data[key]
        return None
