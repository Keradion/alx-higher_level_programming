#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    ''' find multiples of 2 in a list '''
    new_list = my_list[:]
    for each in range(0, len(my_list)):
        if my_list[each] % 2 == 0:
            new_list[each] = 'True'
        else:
            new_list[each] = 'False'
    return new_list
