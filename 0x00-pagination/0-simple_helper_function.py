#!/usr/bin/env python3
"""
simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    return: start and end index in a tuple
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return start_idx, end_idx
