#!/usr/bin/env python3
''' LIFO caching algorithms '''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' inhering from basecahing class '''
    def __init__(self):
        super().__init__()
        self.ls = []

    def put(self, key, item):
        ''' insert key and items to cache_data else
            pass if key or items is none and discard
            from the dic if NO dic is > Max_tems '''
        if key is not None or item is not None:
            if key in self.ls and key not in self.cache_data:
                self.ls.remove(key)
                self.ls.append(key)
            elif key not in self.cache_data:
                self.ls.append(key)
            ky = self.ls[0]
            ky_s = str(ky[0])

        if key is None or item is None:
            pass
        elif key in self.cache_data:
            if self.cache_data[key] == item:
                pass
            else:
                self.cache_data[key] = item
        elif len(self.cache_data) == self.MAX_ITEMS:
            if len(self.ls) > 4:
                del self.ls[0]
            print(f'DISCARD: {ky_s}')
            self.cache_data.pop(ky_s)
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        ''' retriev val by key '''
        if not key:
            return None
        try:
            self.cache_data[key]
        except Exception:
            return None
        if key in self.ls and key in self.cache_data:
            self.ls.remove(key)
            self.ls.append(key)
        elif key in self.cache_data:
            self.ls.append(key)
        if len(self.ls) > 4:
            del self.ls[0]
        return self.cache_data[key]
