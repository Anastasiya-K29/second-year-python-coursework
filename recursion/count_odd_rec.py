#!/usr/bin/env python3
 
import ast
list = ast.literal_eval(input())

def count_odd(list):
    if not list:
        return 0
    
    first = 1 if list[0] % 2 != 0 else 0
    return first + count_odd(list[1:])

print(count_odd(list))