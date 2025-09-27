#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends the built-in list class
with notification messages for modification operations.
"""


class VerboseList(list):
    """
    A list class that extends the built-in list with verbose notifications.

    This class prints notification messages whenever items are added or removed
    from the list using append, extend, remove, or pop methods.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a notification.

        Args:
            item: The item to add to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from an iterable and print a notification.

        Args:
            iterable: An iterable containing items to add to the list
        """

        items_to_add = list(iterable)
        super().extend(items_to_add)
        print(f"Extended the list with [{len(items_to_add)}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list and print a notification.

        Args:
            item: The item to remove from the list

        Raises:
            ValueError: If the item is not found in the list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item at the given index and print a notification.

        Args:
            index (int, optional): The index of the item to remove. 
                                 Defaults to -1 (last item).

        Returns:
            The item that was removed from the list

        Raises:
            IndexError: If the list is empty or index is out of range
        """

        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
