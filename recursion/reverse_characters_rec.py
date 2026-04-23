#!/usr/bin/env python3

s = input()

def reverse_characters_rec(s):
    if len(s) == 0:
        return
    
    reverse_characters_rec(s[1:])
    print(s[0])

reverse_characters_rec(s)