#!/usr/bin/env python3
import csv
import math
from typing import List
'''simple heper pagination '''


def index_range(page, page_size):
    ''' return tuple '''
    a = page * page_size
    b = a - page_size
    return (b, a)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' return list of list of csv '''
        f = self.dataset()
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        idx = index_range(page, page_size)

        a = int(idx[0])
        b = int(idx[1])
        if b > 19419:
            return []
        return f[a: b]
