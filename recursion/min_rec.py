#!/usr/bin/env python3

import ast
list = ast.literal_eval(input())

def min_recursive(list):
    if len(list) == 1:
        return list[0]
    
    min_rest = min_recursive(list[1:])
    return list[0] if list[0] < min_rest else min_rest

print(min_recursive(list))