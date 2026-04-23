#!/usr/bin/env python3
 
s = input()

def skip_sides(s, left, right):
    if left == right or left == right + 1:
        return s[left]
    if left >= right:
        return ''
    
    return s[left] + s[right] + skip_sides(s, left + 2, right - 2)

print(skip_sides(s, 0, len(s) - 2))