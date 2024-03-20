#!/usr/bin/python3

def best_score(a_dictionary):
    ''' Returns a key with the biggest value '''

    max_score = -1
    max_score_key = ''

    if a_dictionary is None:
        return None

    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            max_score_key = key
    return max_score_key
