#!/usr/bin/env python3

import ast
list = ast.literal_eval(input())

def pairwise_sum(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list[0]]
    
    return [list[0] + list[1]] + pairwise_sum(list[2:])

print(pairwise_sum(list))