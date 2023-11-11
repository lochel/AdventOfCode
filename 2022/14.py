#!../.env/bin/python3

from functools import cmp_to_key
from math import prod

import aoc

LINES = [line.split(' -> ') for line in aoc.LINES]
N = len(LINES)


# 1. How many units of sand come to rest before sand starts flowing into the abyss below?
# ----------------------------------------
def problem1():
  # Boundary box
  x0, y0 = 498,4
  x1, y1 = 498,4
  for line in LINES:
    for i,_ in enumerate(line[1:]):
      a,b = line[i-1].split(',')
      c,d = line[i].split(',')
      a, b, c, d = int(a), int(b), int(c), int(d)

      if min(a,c) < x0:
        x0 = min(a,c)
      if min(b,d) < y0:
        y0 = min(b,d)
      if max(a,c) > x1:
        x1 = max(a,c)
      if max(b,d) > y1:
        y1 = max(b,d)


  y0 = min(y0, 0) - 2
  x0 -= 2
  x1 += 2
  y1 += 1

  # Empty cave
  cave = []
  for i in range(y1-y0+1):
    cave.append((x1-x0+1)*['.'])

  # WALLS
  for line in LINES:
    for idx,_ in enumerate(line[1:]):
      a,b = line[idx].split(',')
      c,d = line[idx+1].split(',')
      a, b, c, d = int(a), int(b), int(c), int(d)
      if a == c:
        for i in range(abs(d-b)+1):
          cave[i+min(b,d)-y0][a-x0] = '#'
      elif b == d:
        for i in range(abs(c-a)+1):
          cave[b-y0][min(a,c)+i-x0] = '#'

  # SAND
  answer = 0
  while cave[0-y0][500-x0] == '.':
    sY = 0
    sX = 500
    while True:
      if cave[sY+1-y0][sX-x0] == '.':
        sY += 1
      elif cave[sY+1-y0][sX-1-x0] == '.':
        sX -= 1
        sY += 1
      elif cave[sY+1-y0][sX+1-x0] == '.':
        sX += 1
        sY += 1
      else:
        break
      if sY >= y1:
        print(f'Answer 1: {answer}')
        return
    answer += 1
    cave[sY-y0][sX-x0] = 'o'


# 2. How many units of sand come to rest?
# ----------------------------------------
def problem2():
  x0, y0 = 498,4
  x1, y1 = 498,4
  for line in LINES:
    for i,_ in enumerate(line[1:]):
      a,b = line[i-1].split(',')
      c,d = line[i].split(',')
      a, b, c, d = int(a), int(b), int(c), int(d)

      if min(a,c) < x0:
        x0 = min(a,c)
      if min(b,d) < y0:
        y0 = min(b,d)
      if max(a,c) > x1:
        x1 = max(a,c)
      if max(b,d) > y1:
        y1 = max(b,d)

  y0 = min(y0, 0) - 2
  x0 -= 200
  x1 += 200
  y1 += 2

  # Empty cave
  cave = []
  for i in range(y1-y0+1):
    cave.append((x1-x0+1)*['.'])

  # Walls
  for line in LINES:
    for idx,_ in enumerate(line[1:]):
      a,b = line[idx].split(',')
      c,d = line[idx+1].split(',')
      a, b, c, d = int(a), int(b), int(c), int(d)
      if a == c:
        for i in range(abs(d-b)+1):
          cave[i+min(b,d)-y0][a-x0] = '#'
      elif b == d:
        for i in range(abs(c-a)+1):
          cave[b-y0][min(a,c)+i-x0] = '#'

  # SAND
  answer = 0
  while cave[0-y0][500-x0] == '.':
    sY = 0
    sX = 500
    while True:
      if sY < y1-1:
        if cave[sY+1-y0][sX-x0] == '.':
          sY += 1
        elif cave[sY+1-y0][sX-1-x0] == '.':
          sX -= 1
          sY += 1
        elif cave[sY+1-y0][sX+1-x0] == '.':
          sX += 1
          sY += 1
        else:
          break
      else:
        break
    answer += 1
    cave[sY-y0][sX-x0] = 'o'

  #for x in cave:
  #  for y in x:
  #    print(y, end='')
  #  print('')
  #print('')
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
