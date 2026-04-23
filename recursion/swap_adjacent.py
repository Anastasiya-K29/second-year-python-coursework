#!/usr/bin/env python3
 
s = input()

def swap_adjacent(s):
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s[0]
    return s[1] + s[0] + swap_adjacent(s[2:])

print(swap_adjacent(s))