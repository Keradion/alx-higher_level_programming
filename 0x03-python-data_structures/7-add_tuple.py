#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ''' add 2 tuples '''
    ''' tuple unpacking '''
    if __name__ == '__main__':
        a, b = (tuple_a[0] if len(tuple_a) >= 1 else 0),\
        (tuple_a[1] if len(tuple_a) >= 2 else 0)
        c, d = (tuple_b[0] if len(tuple_b) >= 1 else 0),\
        (tuple_b[1] if len(tuple_b) >= 2 else 0)

    return (a + c), (b + d)
