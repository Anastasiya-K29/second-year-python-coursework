# In each of the following tasks, you will be presented with 
# a sequence. Your task is to output the first ten elements 
# of the sequence to standard output, one per line. Your 
# solutions must make good use of a while loop and must involve 
# at most one print statement, but additionally require you to 
# maintain an extra state variable. you must keep track of the 
# sum of the values of i encountered so far; so you will need 
# an additional variable, total.

# Sequence: 0 1 3 6 10 15 

#!/usr/bin/env python3

i = 0
t = 0

while i < 10:
  t = t + i
  print(t)
  i += 1