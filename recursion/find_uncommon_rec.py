#!/usr/bin/env python3

import ast
a = ast.literal_eval(input())
b = ast.literal_eval(input())

def find_uncommon(a, b):
    if not a and not b:
        return []
    if not a:
        return [b[0]] + find_uncommon(a, b[1:])
    if not b:
        return [a[0]] + find_uncommon(a[1:], b)
    if a[0] not in b:
        return [a[0]] + find_uncommon(a[1:], b)
    else:
        return find_uncommon(a[1:], [x for x in b if x != a[0]])
    
print(find_uncommon(a, b))