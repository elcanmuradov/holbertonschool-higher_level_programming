#!/usr/bin/env python3
"""
This module defines a CountedIterator class that extends iterator functionality
with counting capabilities.
"""


class CountedIterator:
    """
    An iterator wrapper that keeps track of the number of items iterated.

    This class wraps any iterable and provides counting functionality,
    tracking how many items have been fetched through iteration.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args
            iterable: Any iterable object (list, tuple, string, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Get the current count of items that have been iterated.

        Returns:
            int: The number of items that have been fetched so far
        """
        return self.count

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.

        Returns:
            The next item from the iterator

        Raises:
            StopIteration: When there are no more items to iterate
        """
        try:

            item = next(self.iterator)

            self.count += 1
            return item
        except StopIteration:

            raise

    def __iter__(self):
        """
        Return self to make this object iterable.

        This allows the CountedIterator to be used in for loops and
        other contexts that expect an iterable.

        Returns:
            self: The CountedIterator instance
        """
        return self
