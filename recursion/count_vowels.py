#!/usr/bin/env python3

s = input()
vowels = 'aeiou'

def count_vowels_recursive(s):
    if len(s) == 0:
        return 0
    
    if s[0] in vowels:
        return 1 + count_vowels_recursive(s[1:])
    else:
        return 0 + count_vowels_recursive(s[1:])
    
print(count_vowels_recursive(s))