#!/usr/bin/python3

def uniq_add(my_list=[]):
    ''' adds all unique integers in a list '''
    sum_ = 0
    new_set = set(my_list)
    new_list = list(new_set)

    for value in new_list:
        sum_ += value

    return sum_
