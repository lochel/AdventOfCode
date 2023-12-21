#!../.env/bin/python3

import math
import statistics
import sys
from collections import defaultdict, deque
from itertools import combinations
import copy
import aoc

#sys.setrecursionlimit(10000)

# 1.
# ----------------------------------------
def problem1():
  map = aoc.parseLines(aoc.LINES, lambda line : list(line))

  for x,y in aoc.Grid(map):
    if map[y][x] == 'S':
      pos = (x, y)

  Q = deque()
  end = set([pos])
  for _ in range(64):
    Q = deque(end)
    end = set()

    while Q:
      x, y = Q.pop()
      for (xx, yy) in aoc.get_neighbors(x, y, False, True):
        if map[yy][xx] in '.S':
          end.add((xx, yy))

  print(f'Answer 1: {len(end)}')

# 2.
# ----------------------------------------
def problem2():
  # - In exactly 6 steps, he can still reach 16 garden plots.
  # - In exactly 10 steps, he can reach any of 50 garden plots.
  # - In exactly 50 steps, he can reach 1594 garden plots.
  # - In exactly 100 steps, he can reach 6536 garden plots.
  # - In exactly 500 steps, he can reach 167004 garden plots.
  # - In exactly 1000 steps, he can reach 668697 garden plots.
  # - In exactly 5000 steps, he can reach 16733044 garden plots.

  map = aoc.parseLines(aoc.LINES, lambda line : list(line))

  for x,y in aoc.Grid(map):
    if map[y][x] == 'S':
      pos = (x, y)



  Q = deque()
  end = defaultdict(set)
  end[pos].add((0, 0))
  for step in range(10):
    Q = deque(end.items())
    end.clear()

    while Q:
      (x, y), z = Q.pop()
      for (xx, yy) in aoc.get_neighbors(x, y, False, False):
        if map[yy % aoc.N][xx % aoc.M] in '.S':
          end[(xx, yy)] = z
    print(step, sum([len(x) for x in end.values()]))
  answer = sum([len(x) for x in end.values()])
  print(f'Answer 2: {answer}')





  end.clear()
  end[pos].add((0, 0))
  for step in range(10):
    Q = deque(end.items())
    end.clear()

    while Q:
      (x, y), z = Q.pop()
      for (xx, yy) in aoc.get_neighbors(x, y, False, False):
        if map[yy % aoc.N][xx % aoc.M] in '.S':
          end[(xx % aoc.M, yy % aoc.N)].add((xx//aoc.M, yy//aoc.N))
          for zz in z:
            end[(xx % aoc.M, yy % aoc.N)].add(zz)
    print(step, sum([len(x) for x in end.values()]))
  answer = sum([len(x) for x in end.values()])
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
