#!/usr/bin/python3
def multiple_returns(sentence):
    ''' Return tuple with length and first charachter of string '''

    length = len(sentence)
    if sentence == '':
        first = None
    else:
        first = sentence[0]
    return length, first
