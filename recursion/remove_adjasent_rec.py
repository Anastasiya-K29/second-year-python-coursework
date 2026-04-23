#!/usr/bin/env python3

text = input()

def remove_adjacent(text):
    if len(text) <= 1:
        return text
    
    if text[0] == text[1]:
        return remove_adjacent(text[1:])
    
    return text[0] + remove_adjacent(text[1:])

print(remove_adjacent(text))