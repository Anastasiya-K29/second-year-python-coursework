# Write a Python script which reads a positive integer n 
# from standard input and outputs the first n terms of the 
# sequence:
# - n-1 n-2 n-3 … 0

#!/usr/bin/env python3

n = int(input())

i = n - 1
while i >= 0:
  print(i)
  i -= 1