#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """
    class MyList inherits from list
    """

    def print_sorted(self):
        """
        Method for print sorted_list
        """
        print(sorted(self))
