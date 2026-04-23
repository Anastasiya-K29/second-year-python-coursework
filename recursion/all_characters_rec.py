#!/usr/bin/env python3

s = input()

def all_characters_recursive(s):
    if len(s) == 0:
        return
    
    print(s[0])
    all_characters_recursive(s[1:])

all_characters_recursive(s)