#!/usr/bin/python3

def max_integer(my_list=[]):
    ''' find max item in a list '''
    max_item = 0

    if my_list == []:
        return None

    for each in range(0, (len(my_list))):
        if my_list[each] > max_item:
            max_item = my_list[each]
    return max_item
