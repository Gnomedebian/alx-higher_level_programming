#!/usr/bin/python3
"""function inherits_from"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance
    of a class that inherited from the specified class,
    False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
