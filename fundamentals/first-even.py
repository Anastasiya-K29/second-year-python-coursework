# Write a Python script which reads a sequence of 
# integers from standard input and outputs only the 
# first even number encountered.

#!/usr/bin/env python3

import sys

line = sys.stdin.readline()
while line:
  num = int(line.strip())
  if num % 2 == 0:
    print(num)
    sys.exit(0)
  line  = sys.stdin.readline()