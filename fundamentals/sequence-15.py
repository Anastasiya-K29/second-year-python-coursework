# Write a Python script which reads a positive integer 
# n from standard input and outputs the first n terms 
# of the sequence:
# - 1 2 4 8 16 32

#!/usr/bin/env python3

n = int(input())
i = 0
t = 1
while i < n:
  print(t)
  t = t * 2
  i += 1