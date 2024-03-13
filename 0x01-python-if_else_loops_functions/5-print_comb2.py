#!/usr/bin/python3

for each in range(0, 100):
    if each == 99:
        print('{}'.format(each))
    else:
        print('{:02d}, '.format(each), end='')
