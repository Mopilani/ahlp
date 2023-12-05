#!/usr/bin/python3

""" Return true if instance is of type class """


def inherits_from(obj, a_class):
    """ Return true if instance is of type class """
    return isinstance(obj, a_class) and type(obj) is not a_class

