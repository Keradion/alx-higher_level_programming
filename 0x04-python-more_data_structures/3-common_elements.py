#!/usr/bin/python3
def common_elements(set_1, set_2):
    ''' Returns a set of common elements in two sets '''
    common_values = set_1.intersection(set_2)
    return set(common_values)
