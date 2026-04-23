#!/usr/bin/env python3

import ast
 
a = ast.literal_eval(input())
b = ast.literal_eval(input())

def merge_lists (a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    
    if a[0] <= b[0]:
        return [a[0]] + merge_lists(a[1:], b)
    else:
        return [b[0]] + merge_lists(a, b[1:])
    
print(merge_lists(a, b))