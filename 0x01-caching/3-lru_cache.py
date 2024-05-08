#!/usr/bin/env python3
''' lru caching '''
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    ''' LRU cache '''
    def __init__(self):
        ''' init '''
        super().__init__()
        self.access_order = OrderedDict()

    def put(self, key, item):
        ''' insert a key and val '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.access_order[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            oldest_key = next(iter(self.access_order))
            print(f'DISCARD: {oldest_key}')
            del self.cache_data[oldest_key]
            del self.access_order[oldest_key]

        self.cache_data[key] = item
        self.access_order[key] = None

    def get(self, key):
        ''' retriev a key '''
        if key not in self.cache_data:
            return None

        del self.access_order[key]
        self.access_order[key] = None

        return self.cache_data[key]
