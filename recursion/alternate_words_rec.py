#!/usr/bin/env python3
 
s1 = input()
s2 = input()

def interleave(s1, s2):
    if len(s1) == 0:
        return ''
    
    return s1[0] + s2[0] + interleave(s1[1:], s2[1:])

print(interleave(s1, s2))