#!/usr/bin/env python3

import ast
list = ast.literal_eval(input())

def missing_positive(list, curr=1):
    if curr not in list:
        return curr
    
    return missing_positive(list, curr + 1)

print(missing_positive(list))