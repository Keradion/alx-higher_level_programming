#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ''' add elements of tuples '''
    sum_ = ()
    for each in tuple_a:
        for every in tuple_b:
            sum_ = sum_ + ((each + every),)
