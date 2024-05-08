#!/usr/bin/env python3
''' basic caching '''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' inhering from basecaching class '''
    def put(self, key, item):
        ''' insert key and val to the cache_data
            if key or item are none pass
            '''
        if key and item:
            self.cache_data[key] = item

    def get(self,  key):
        ''' return val of key in cache_data
            return none if key doesn't exist or
            key is none '''
        if not key:
            return None
        try:
            self.cache_data[key]
        except Exception:
            return None
        return self.cache_data[key]
