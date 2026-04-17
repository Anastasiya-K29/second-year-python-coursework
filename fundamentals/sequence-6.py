# In each of the following tasks, you will be presented with 
# a sequence. Your task is to output the first ten elements 
# of the sequence to standard output, one per line. Your 
# solutions must make good use of a while loop and must involve 
# at most one print statement.

# Sequence: 0 1 2 0 1 2 0 

#!/usr/bin/env python3

i = 0
n = 0
while n < 10:
  print(i)
  i = (i + 1) % 3
  n += 1