#!/usr/bin/env python3

import ast
 
list = ast.literal_eval(input())

def is_sorted(list):
    if len(list) <= 1:
        return True
    
    if list[0] > list[1]:
        return False
    
    return is_sorted(list[1:])

print(is_sorted(list))