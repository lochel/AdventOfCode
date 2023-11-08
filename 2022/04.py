#!../.env/bin/python3

import os.path
import sys
from collections import defaultdict

input_file = sys.argv[1] if len(sys.argv) > 1 else os.path.splitext(sys.argv[0])[0] + '.in'
LINES = [line.strip() for line in open(input_file)]
N = len(LINES)
print(f'input contains {N} lines')


# 1. In how many assignment pairs does one range fully contain the other?
# --------------------------------------
def problem1():
  answer = 0
  for line in LINES:
    [a, b] = line.split(',')
    a = [int(i) for i in a.split('-')]
    b = [int(i) for i in b.split('-')]
    if a[0] <= b[0] and a[1] >= b[1]:
      answer += 1
    elif a[0] >= b[0] and a[1] <= b[1]:
      answer += 1
  return answer


# 2. In how many assignment pairs do the ranges overlap?
# --------------------------------------
def problem2():
  answer = 0
  for line in LINES:
    [a, b] = line.split(',')
    a = [int(i) for i in a.split('-')]
    b = [int(i) for i in b.split('-')]
    if a[0] <= b[0] <= a[1]:
      answer += 1
    elif a[0] <= b[1] <= a[1]:
      answer += 1
    elif b[0] <= a[0] <= b[1]:
      answer += 1
    elif b[0] <= a[1] <= b[1]:
      answer += 1
  return answer


# --------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {problem1()}')
  print(f'Answer 2: {problem2()}')
