#!/usr/bin/python3

def no_c(my_string):
    ''' removes all charachters from a string '''
    new_string = ''
    for each in range(0, (len(my_string))):
        if my_string[each] == 'c' or my_string[each] == 'C':
            continue
        new_string = new_string + my_string[each]
    return new_string
