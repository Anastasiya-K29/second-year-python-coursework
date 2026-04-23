#!/usr/bin/env python3

import ast 
list = ast.literal_eval(input())

def sum_list(list):
    if list == []:
        return 0
    
    return list[0] + sum_list(list[1:])

print(sum_list(list))