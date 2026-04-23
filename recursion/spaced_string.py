#!/usr/bin/env python3
 
s = input()

def spaced_string(s):
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s[0]
    return s[0] + ' ' + spaced_string(s[1:])

print(spaced_string(s))