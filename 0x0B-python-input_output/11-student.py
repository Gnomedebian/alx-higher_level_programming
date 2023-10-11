#!/usr/bin/python3
"""class student"""


class Student:
    """
    defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retunr a dictionary"""
        if type(attrs) is list and all(type(t) is str for t in attrs):
            return {k: vl for k, vl in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replaces attributes of the Student instance"""
        for k, value in json.items():
            self.__dict__[k] = value
