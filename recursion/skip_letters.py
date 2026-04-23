#!/usr/bin/env python3
 
s = input()

def skip_letters(s):
    if len(s) < 2:
        return ''
    return s[1] + skip_letters(s[2:])

print(skip_letters(s))