#!/usr/bin/env python3
""" Simple helper function """


def index_range(page, page_size):
    """
    Return a tuple of size two
    containing a start index and an end
    index corresponding to
    the range of indexes to return in a list for
    those particular pagination parameters
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    before = (page - 1) * page_size
    return (before, before + page_size)
