#!/usr/bin/env python3

import ast
list = ast.literal_eval(input())

def pairwise_sop(list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list[0]]
    
    pair_sum = list[0] + list[1]
    pair_product = list[0] * list [0]

    if pair_sum % 2 == 0:
        return [pair_sum] + pairwise_sop(list[2:])
    else:
        return [pair_product] + pair_product(list[2:])

print(pairwise_sop(list))