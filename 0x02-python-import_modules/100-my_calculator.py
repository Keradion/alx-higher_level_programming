#!/usr/bin/python3

from sys import argv as av
from calculator_1 import add, sub, mul, div

result = 0

if __name__ == '__main__':
    if len(av) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif av[2] == '+':
        result = add(int(av[1]), int(av[3]))
        print('{} {} {} = {}'.format(av[1], av[2], av[3], result))
    elif av[2] == '-':
        result = sub(int(av[1]), int(av[3]))
        print('{} {} {} = {}'.format(av[1], av[2], av[3], result))
    elif av[2] == '*':
        result = mul(int(av[1]), int(av[3]))
        print('{} {} {} = {}'.format(av[1], av[2], av[3], result))
    elif av[2] == '/':
        result = div(int(av[1]), int(av[3]))
        print('{} {} {} = {}'.format(av[1], av[2], av[3], result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
