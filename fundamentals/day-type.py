# Write a Python script which reads a day and outputs either 
# the message weekend or the message weekday, as appropriate.

#!/usr/bin/env python3
 
day = int(input())

if day < 5:
  print('weekday')
else:
  print('weekend')