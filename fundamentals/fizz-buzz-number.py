# Write a Python script which reads a single positive integer 
# from standard input and outputs the corresponding fizz-buzz output:
# - if the number is divisible by 5 and by 3 then output fizz-buzz,
# - otherwise if the number is divisible by 3 then output fizz,
# - otherwise if the number is divisible by 5 then output buzz,
# - otherwise output the number itself.

#!/usr/bin/env python3

num = int(input())
 
if num % 5 == 0 and num % 3 == 0:
  print('fizz-buzz')
elif num % 5 == 0:
  print('buzz')
elif num % 3 == 0:
  print('fizz')
else:
  print(num)