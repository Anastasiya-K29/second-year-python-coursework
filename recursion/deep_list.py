#!/usr/bin/env python3

import ast
 
list = ast.literal_eval(input())

def deep_list(list, depth=0, result=None):
    if result is None:
        result = {}

    for item in list:
        if isinstance(item, list):
            deep_list(item, depth + 1, result)
        else:
            if depth not in result:
                result[depth] = []
            result[depth].append(item)

    return result

print(deep_list(list))