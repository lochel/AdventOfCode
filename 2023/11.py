#!../.env/bin/python3

import math
import statistics
import sys
from collections import defaultdict, deque
from itertools import combinations

import aoc

#sys.setrecursionlimit(10000)

# 1.
# ----------------------------------------
def problem1():
  #lines = aoc.LINES
  lines = aoc.parseLines(aoc.LINES, lambda line: list(line))

  mapY = []
  for y in range(aoc.N):
    if any([x == '#' for x in lines[y]]):
      mapY.append(lines[y])
    else:
      mapY.append(['.']*aoc.M)
      mapY.append(['.']*aoc.M)

  map = []
  for y in range(len(mapY)):
    map.append([])

  for x in range(aoc.M):
    if any([mapY[y][x] == '#' for y in range(len(mapY))]):
      for y in range(len(mapY)):
        map[y].append(mapY[y][x])
    else:
      for y in range(len(mapY)):
        map[y].append('.')
        map[y].append('.')

  print()
  galaxies = []
  for (x, y) in aoc.Grid(map):
    if map[y][x] == '#':
      galaxies.append((x, y))

  answer = 0
  for (x1, y1), (x2, y2) in combinations(galaxies, 2):
    answer += abs(x1-x2) + abs(y1-y2)

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.parseLines(aoc.LINES, lambda line: list(line))

  d = 1000000

  mapY = []
  for y in range(aoc.N):
    if any([x == '#' for x in lines[y]]):
      mapY.append(lines[y])
    else:
      mapY.append([d]*aoc.M)

  map = []
  for y in range(len(mapY)):
    map.append([])

  for x in range(aoc.M):
    if any([mapY[y][x] == '#' for y in range(len(mapY))]):
      for y in range(len(mapY)):
        map[y].append(mapY[y][x])
    else:
      for y in range(len(mapY)):
        map[y].append(d)

  galaxies = []
  for (x, y) in aoc.Grid(map):
    if map[y][x] == '#':
      galaxies.append((x, y))

  for (x, y) in aoc.Grid(map):
    if map[y][x] != d:
      map[y][x] = 1

  #print()
  #for line in map:
  #  print(line)

  answer = 0
  for (x1, y1), (x2, y2) in combinations(galaxies, 2):
    for y in range(min(y1, y2), max(y1, y2)):
      answer += map[y][x2]
    for x in range(min(x1, x2), max(x1, x2)):
      answer += map[y2][x]
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
