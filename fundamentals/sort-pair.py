# Write a Python script named which reads exactly two integers 
# from standard input, one per line, and outputs those numbers 
# in increasing order (on a single line).

#!/usr/bin/env python3

a = int(input())
b = int(input())

if a > b:
  print(b , a)
else:
  print(a, b)