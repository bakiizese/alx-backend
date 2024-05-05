#!/usr/bin/env python3
'''simple heper pagination '''


def index_range(page, page_size):
    ''' return tuple '''
    a = page * page_size
    b = a - page_size
    return (b, a)
