#!/usr/bin/python3

for each in range(0, 10):
    for every in range(0, 10):
        if each == 8 and every == 9:
            print('{}{}'.format(each, every))
        elif each != every and each < every:
            print('{}{}, '.format(each, every), end='')
