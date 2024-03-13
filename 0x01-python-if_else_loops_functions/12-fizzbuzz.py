#!/usr/bin/python3

def fizzbuzz():
    for each in range(1, 101):
        if each % 3 == 0:
            print('{}'.format('Fizz'), end=' ')
        elif each % 5 == 0:
            print('{}'.format('Buzz'), end=' ')
        elif each % 3 == 0 and each % 5 == 0:
            print('{}'.format('FizzBuzz'), end='')
        else:
            print('{}'.format(each), end=' ')
