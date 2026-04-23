#!/usr/bin/env python3
 
import ast
 
a = ast.literal_eval(input())
b = ast.literal_eval(input())

def sum_two_lists(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    return [a[0] + b[0]] + sum_two_lists(a[1:], b[1:])

print(sum_two_lists(a, b))