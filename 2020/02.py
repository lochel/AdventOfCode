#!../.env/bin/python3

import itertools
import math
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else '02.in'
LINES = [line.strip().split(" ") for line in open(input_file)]

# 1.
# ----------------------------------------
def problem1():
  valid = 0
  for line in LINES:
    a = int(line[0])
    b = int(line[1])
    c = line[3].count(line[2])
    if a <= c <= b:
      valid+=1
  print(f'Answer 1: {valid}')

# 2.
# ----------------------------------------
def problem2():
  valid = 0
  for line in LINES:
    a = int(line[0])
    b = int(line[1])
    if line[3][a-1] == line[2] and line[3][b-1] != line[2]:
      valid+=1
    elif line[3][a-1] != line[2] and line[3][b-1] == line[2]:
      valid+=1
  print(f'Answer 2: {valid}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
