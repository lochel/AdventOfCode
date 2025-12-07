#!../.env/bin/python3

import math
import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  pos = set([lines[0].index('S')])

  answer = 0
  for line in lines[1:]:
    for p in list(pos):
      if line[p] == '^':
        pos.add(p-1)
        pos.add(p+1)
        pos.remove(p)
        answer += 1

  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  paths = {lines[0].index('S'): 1}

  for line in lines[1:]:
    for p in list(paths.keys()):
      if line[p] == '^':
        paths[p-1] = paths.get(p-1, 0) + paths.get(p, 0)
        paths[p+1] = paths.get(p+1, 0) + paths.get(p, 0)
        paths.pop(p)

  answer = sum(paths.values())
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
