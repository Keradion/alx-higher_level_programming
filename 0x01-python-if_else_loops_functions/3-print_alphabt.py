#!/usr/bin/python3
for each in range(97, 123):
    if chr(each) == 'q' or chr(each) == 'e':
        continue
    print('{}'.format(chr(each)), end='')
