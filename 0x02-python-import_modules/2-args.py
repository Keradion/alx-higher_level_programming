#!/usr/bin/python3

import sys
''' arguments stored in argv attribute of the sys module '''

if __name__ == '__main__':
    for each in range(len(sys.argv) - 1):
        if len(sys.argv) == 1:
            print('{} arguments.'.format(0))
        elif len(sys.argv) == 2:
            print('{} argument:'.format(1))
            print('{}: {}'.format(1, sys.argv[1]))
            break
        else:
            print('{}: {}'.format(each + 1, sys.argv[each + 1]))
