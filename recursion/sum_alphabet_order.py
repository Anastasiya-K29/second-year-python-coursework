#!/usr/bin/env python3

s = input()

def sum_alphabet_order(s):
    if len(s) == 0:
        return 0

    position = ord(s[0].lower()) - ord('a') + 1
    return position + sum_alphabet_order(s[1:])

print(sum_alphabet_order(s))