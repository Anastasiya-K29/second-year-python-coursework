#!/usr/bin/env python3
 
s = input()

def every_other_from_end(s):
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s[0]
    return s[-1] + every_other_from_end(s[:-2])

print(every_other_from_end(s))