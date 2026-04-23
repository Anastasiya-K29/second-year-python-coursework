#!/usr/bin/env python3
 
s = input()

def outside_in(s):
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s[0]
    return s[0] + s[-1] + outside_in(s[1:-1])

print(outside_in(s))