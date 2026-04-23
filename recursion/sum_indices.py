#!/usr/bin/env python3 

s = input()
target = input()

def sum_indices(s, target, index):
    if index == len(s):
        return 0

    if s[index] == target:
        return index + sum_indices(s, target, index + 1)
    else:
        return sum_indices(s, target, index + 1)

print(sum_indices(s, target, 0))