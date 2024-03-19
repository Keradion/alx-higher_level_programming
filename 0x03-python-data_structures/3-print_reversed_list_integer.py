#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    ''' Print elements of a list in reverse '''
    if my_list == [] or my_list == None:
        return
    for each in range((len(my_list) - 1), -1, -1):
        print('{:d}'.format(my_list[each]))
