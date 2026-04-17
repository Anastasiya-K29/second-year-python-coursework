# Write a Python script which outputs only the sum 
# of the numbers on standard input.

#!/usr/bin/env python3
  
import sys
 
t = 0
 
for line in sys.stdin:
  num = int(line)
  if num == 0:
    break
  t += num

print(t)