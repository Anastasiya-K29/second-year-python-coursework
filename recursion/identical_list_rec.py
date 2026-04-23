#!/usr/bin/env python3

import ast
list = ast.literal_eval(input())

def identical_list_recursive(list):
    if len(list) <= 1:
        return True
 
    if list[0] != list[1]:
        return False
 
    return identical_list_recursive(list[1:])

print(identical_list_recursive(list))