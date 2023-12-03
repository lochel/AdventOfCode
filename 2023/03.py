#!../.env/bin/python3

import math
from collections import defaultdict

import aoc

LINES = aoc.LINES

def adjacent_symbol(x, y):
  A = aoc.get_neighbors(x, y)

  for (x, y) in A:
    if LINES[y][x] not in '0123456789.':
      return True
  return False

def might_be_gear(x, y):
  A = aoc.get_neighbors(x, y)

  for (x, y) in A:
    if LINES[y][x] in '*':
      return True, (x, y)
  return False, None

# 1.
# ----------------------------------------
def problem1():
  answer = 0
  for (x, y) in aoc.Grid(LINES):
    if x == 0:
      number = ''
      part = False

    if LINES[y][x] in '0123456789':
      number += LINES[y][x]
      part = part or adjacent_symbol(x, y)

    if LINES[y][x] not in '0123456789' or x+1 == aoc.M:
      if number != '':
        if part:
          answer += int(number)
        number = ''
        part = False

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  gear_ratio = defaultdict(list)
  for (x, y) in aoc.Grid(LINES):
    if x == 0:
      number = ''
      gear = False
      pos = None

    if LINES[y][x] in '0123456789':
      number += LINES[y][x]
      a, b = might_be_gear(x, y)
      if a:
        gear = True
        pos = b

    if LINES[y][x] not in '0123456789' or x+1 == aoc.M:
      if number != '':
        if gear:
          gear_ratio[pos].append(int(number))
        number = ''
        gear = False
        pos = None

  answer = 0
  for gear in gear_ratio.values():
    if (len(gear) == 2):
      answer += math.prod(gear)

  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
