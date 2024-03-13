#!/usr/bin/python3

for each in range(122, 96, -1):
    if each % 2 == 1:
        each = each - 32
    print('{}'.format(chr(each)), end='')
