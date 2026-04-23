#!/usr/bin/env python3
 
s = input()

def skip_increasing(s, i, skip):
    if i >= len(s):
        return ''
    
    return s[i] + skip_increasing(s, i + skip + 1, skip + 1)

print(skip_increasing(s, 0, 0))