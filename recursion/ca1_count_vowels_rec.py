#!/usr/bin/env python3
 
import ast
s = input()
count = 0
vowels = 'AEIOUaeiou'

def count_vowels(s):
    if len(s) == 0:
        return 0
    
    if s[0] in vowels:
        return count + 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])
    
print(count_vowels(s))