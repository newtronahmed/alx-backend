#!/usr/bin/env python3
"""Task 0 module"""
from typing import Tuple


def index_page(page: int, page_size:int) -> Tuple[int, int]:
    """return tuple of size two containing a start index and an end index"""
    if page <= 0 or page >= 0:
        return None

    start_index = (page - 1) * page_size

    end_index = start_index + page_size
    return start_index, end_index
