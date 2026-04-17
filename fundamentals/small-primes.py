# Write a Python script that when reads two integers, first the number 
# of goals in a gaelic football match and then the number of points, 
# and outputs the total score.

#!/usr/bin/env python3

n = int(input())
n > 20
 
if n == 2 and n == 3:
  print(n, ' prime')
elif n % 2 == 0 or n % 3 == 0 or n == 1:
  print(n, 'not prime')
else:
  print(n, 'prime')