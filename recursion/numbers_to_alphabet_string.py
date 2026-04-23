#!/usr/bin/env python3

import ast
lst = ast.literal_eval(input())

def numbers_to_alphabet_string(lst):
    if len(lst) == 0:
        return ""

    if lst[0] >= 1 and lst[0] <= 26:
        letter = chr(ord('a') + lst[0] - 1)
        return letter + numbers_to_alphabet_string(lst[1:])
    else:
        return numbers_to_alphabet_string(lst[1:])

print(numbers_to_alphabet_string(lst))