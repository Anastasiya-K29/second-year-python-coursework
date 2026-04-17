# Write a Python script which reads exactly three positive 
# integers from standard input (one per line) and outputs 
# either the message yes or the message no to indicate whether 
# it is possible to form a triangle with sides of these lengths or not.

#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
  longest = a
elif b > a and b > c:
  longest = b
else:
  longest = c
 
r = (a + b + c) - longest
 
if r > longest:
  print('yes')
else:
   print('no')