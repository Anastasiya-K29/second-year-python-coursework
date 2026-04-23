#!/usr/bin/env python3

import ast
list = ast.literal_eval(input())

def pairwise_product(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list[0]]
    
    return [list[0] * list[1]] + pairwise_product(list[2:])

print(pairwise_product(list))