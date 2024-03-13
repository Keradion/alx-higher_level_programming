#!/usr/bin/python3

def remove_char_at(str, n):

    string_copy = ''

    for index in range(len(str)):
        if index == n:
            continue
        string_copy = string_copy + str[index]

    return string_copy
