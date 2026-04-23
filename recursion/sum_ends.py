#!/usr/bin/env python3

import ast
list = ast.literal_eval(input())

def sum_ends(list):
    if len(list) == 0:
        return []
    
    if len(list) == 1:
        return [list[0]]
    
    return [list[0] + list[-1]] + sum_ends(list[1:-1])

print(sum_ends(list))