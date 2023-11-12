#!../.env/bin/python3

import itertools
import math
import aoc

aoc.parseLines(int)

# 1.
# ----------------------------------------
def problem1():
  combinations = itertools.combinations(aoc.LINES, 2)
  for c in combinations:
    if sum(c) == 2020:
      answer = math.prod(c)
      print(f'Answer 1: {answer} with {c}')

# 2.
# ----------------------------------------
def problem2():
  combinations = itertools.combinations(aoc.LINES, 3)
  for c in combinations:
    if sum(c) == 2020:
      answer = math.prod(c)
      print(f'Answer 2: {answer} with {c}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
