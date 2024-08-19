#!/usr/bin/env python3
"""This module contains index_range() function and Server class"""

import csv
import math
from typing import List, Tuple
import csv


def index_range(page, page_size) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """

    end_index = page_size * page
    start_index = end_index - page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
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
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        with open('Popular_Baby_Names.csv', 'r') as file:
            csv_reader = csv.reader(file)
            start_index, end_index = index_range(page, page_size)
            csv_list = list(csv_reader)
            csv_list = csv_list[1:]
            if start_index >= len(csv_list) or end_index >= len(csv_list):
                return []
            return csv_list[start_index: end_index]
