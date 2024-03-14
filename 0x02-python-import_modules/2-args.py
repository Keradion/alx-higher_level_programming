#!/usr/bin/python3

import sys
''' arguments stored in argv attribute of the sys module '''

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('{} arguments.'.format(0))
    elif len(sys.argv) == 2:
        print('{} argument:'.format(1))
        print('{}: {}'.format(each, sys.argv[1]))
    else:
        print('{} arguments:'.format(len(sys.argv) - 1))
        for each in range(1, len(sys.argv)):
            print('{}: {}'.format(each, sys.argv[each]))
