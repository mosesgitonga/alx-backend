#!/usr/bin/env python3
"""
simple pagination
"""
import math
import csv
from typing import List


def index_range(page, page_size, total_items):
    """
    Calculate start and end indices for pagination.

    Parameters:
    - page: Current page number (1-indexed).
    - page_size: Number of items to display on each page.
    - total_items: Total number of items in the dataset.

    Returns:
    - start_index: Starting index of the current page.
    - end_index: Ending index of the current page.
    """
    if page < 1 or page_size < 1 or total_items < 0:
        raise ValueError("Invalid page, page_size, or total_items values.")

    # Calculate start and end indices
    start_index = (page - 1) * page_size
    end_index = min(start_index + page_size - 1, total_items - 1)

    return start_index, end_index

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
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:]
            except FileNotFoundError:
                self.__dataset = []

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_idx, end_idx = index_range(page, page_size, len(self.dataset()))
        return self.dataset()[start_idx:end_idx]
