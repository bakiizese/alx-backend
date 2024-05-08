#!/usr/bin/env python3
''' FIFO caching algorithms '''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' inhering from basecahing class '''
    def put(self, key, item):
        ''' insert key and items to cache_data else
            pass if key or items is none and discard
            from the dic if NO dic is > Max_tems '''
        if key is None or item is None:
            pass
        elif key in self.cache_data:
            pass
        elif len(self.cache_data) == self.MAX_ITEMS:
            for k, val in self.cache_data.items():
                ky = k
                self.cache_data.pop(k)
                print(f'DISCARD: {ky}')
                self.cache_data[key] = item
                break
        else:
            self.cache_data[key] = item

    def get(self, key):
        ''' retriev val by key '''
        if not key:
            print('s')
            return None
        try:
            self.cache_data[key]
        except Exception:
            print('e')
            return None
        return self.cache_data[key]
