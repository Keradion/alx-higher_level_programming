#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    ''' Returns a set of all elements present only in 1 set '''
    symmetric_differences = set_1.symmetric_difference(set_2)

    return symmetric_differences
