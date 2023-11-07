#!../.env/bin/python3

import itertools
import math
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else '01.in'
LINES = [int(line.strip()) for line in open(input_file)]

# 1.
# ----------------------------------------
def problem1():
  combinations = itertools.combinations(LINES, 2)
  for c in combinations:
    if sum(c) == 2020:
      answer = math.prod(c)
      print(f'Answer 1: {answer} with {c}')

# 2.
# ----------------------------------------
def problem2():
  combinations = itertools.combinations(LINES, 3)
  for c in combinations:
    if sum(c) == 2020:
      answer = math.prod(c)
      print(f'Answer 1: {answer} with {c}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
