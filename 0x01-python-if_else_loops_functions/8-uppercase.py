#!usr/bin/python3

def uppercase(str):
    for each in str:
        if ord(each) >= 97 and ord(each) <= 123:
            print('{}'.format(chr(ord(each) - 32)), end='')
        else:
            print('{}'.format(each), end='')
