#!/usr/bin/python3

for each in range(0, 100):
    if each < 10:
        print('{}{}, '.format(0, each), end='')
    elif each == 99:
        print(99)
    else:
        print('{}, '.format(each), end='')
