# Write a Python script which outputs only a count 
# of the numbers on standard input.

#!/usr/bin/env python3

import sys

line = sys.stdin.readline()

count = 0
seen = []
while line:
  if line not in seen:
    count += 1
    seen.append(line)
  line = sys.stdin.readline()

print(len(seen))