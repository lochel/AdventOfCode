#!../.env/bin/python3

import math
from collections import defaultdict

import aoc

LINES = aoc.LINES

def adjacent_symbol(x, y):
  A = []
  A.append((x-1, y-1))
  A.append((x  , y-1))
  A.append((x+1, y-1))
  A.append((x-1, y))
  A.append((x+1, y))
  A.append((x-1, y+1))
  A.append((x  , y+1))
  A.append((x+1, y+1))

  for (x, y) in A:
    if x >= 0 and x<aoc.N:
      if y >= 0 and y<aoc.M:
        if LINES[y][x] not in '0123456789.':
          return True
  return False

def might_be_gear(x, y):
  A = []
  A.append((x-1, y-1))
  A.append((x  , y-1))
  A.append((x+1, y-1))
  A.append((x-1, y))
  A.append((x+1, y))
  A.append((x-1, y+1))
  A.append((x  , y+1))
  A.append((x+1, y+1))

  for (x, y) in A:
    if x >= 0 and x<aoc.N:
      if y >= 0 and y<aoc.M:
        if LINES[y][x] in '*':
          return True, (x, y)
  return False, (-1, -1)

# 1.
# ----------------------------------------
def problem1():
  answer = 0
  for y in range(aoc.M):
    number = ''
    part = False
    for x in range(aoc.N):
      if LINES[y][x] in '0123456789':
        number += LINES[y][x]
        part = part or adjacent_symbol(x, y)
      elif number != '':
        if part:
          answer += int(number)
        number = ''
        part = False
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
  for y in range(aoc.M):
    number = ''
    star = False
    starpos = (-1, -1)
    for x in range(aoc.N):
      if LINES[y][x] in '0123456789':
        number += LINES[y][x]
        a, b = might_be_gear(x, y)
        if a:
          star = True
          starpos = b
      elif number != '':
        if star:
          gear_ratio[starpos].append(int(number))
        number = ''
        star = False
        starpos = (-1, -1)
    if number != '':
      if star:
        gear_ratio[starpos].append(int(number))
      number = ''
      star = False
      starpos = (-1, -1)

  answer = 0
  for gear in gear_ratio.values():
    if (len(gear) == 2):
      answer += math.prod(gear)

  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
