#!/usr/bin/env python3
 
import ast
list = ast.literal_eval(input())

def deep_list(list, depth, result):
    for item in list:
        if isinstance(item, list):
            deep_list(item, depth + 1, result)
        else:
            if depth not in result:
                result[depth] = []
            result[depth].append(item)
        return result
result = {}
print(deep_list(list, 0, result))