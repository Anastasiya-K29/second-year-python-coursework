#!/usr/bin/env python3

import ast
list = ast.literal_eval(input())

def sum_even(list):
    if not list:
        return 0
    first = list[0] if list[0] % 2 else 0
    return first + sum_even(list[1:])

print(sum_even(list))