#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    ''' Replaces or adds key / value in a dictionary '''
    old_dict = a_dictionary

    if key not in old_dict:
        old_dict[key] = value
    else:
        old_dict.update({key: value})

    return old_dict
