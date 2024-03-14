#!/usr/bin/python3

import sys

sum_of_arguments = 0

if len(sys.argv) == 1:
    print('{}'.format(0))
    exit()

for each in range(1, len(sys.argv)):
    sum_of_arguments = sum_of_arguments + int(sys.argv[each])

print('{}'.format(sum_of_arguments))
