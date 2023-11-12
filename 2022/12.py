#!../.env/bin/python3

import sys
from aoc import LINES

sys.setrecursionlimit(10000)

MAX_Y = len(LINES)
MAX_X = len(LINES[0])


# 1. What is the fewest steps required to move from your current position to the location that should get the best signal?
# ------------------------------------------------------------------------------
def problem1():
  SOLUTION = []
  def next(curr, count, map, target, visited):
    if curr == target:
      SOLUTION.append(count)
      return

    (x,y) = curr
    nextCount = count + 1

    if x-1 >= 0 and map[curr]+1 >= map[(x-1,y)]:
      if ((x-1,y) in visited and visited[(x-1,y)] > nextCount) or (x-1,y) not in visited:
        visited[(x-1,y)] = nextCount
        next((x-1,y), nextCount, map, target, visited)
    if y-1 >= 0 and map[curr]+1 >= map[(x,y-1)]:
      if ((x,y-1) in visited and visited[(x,y-1)] > nextCount) or (x,y-1) not in visited:
        visited[(x,y-1)] = nextCount
        next((x,y-1), nextCount, map, target, visited)
    if x+1 < MAX_X and (map[curr]+1 >= map[(x+1,y)]):
      if ((x+1,y) in visited and visited[(x+1,y)] > nextCount) or (x+1,y) not in visited:
        visited[(x+1,y)] = nextCount
        next((x+1,y), nextCount, map, target, visited)
    if y+1 < MAX_Y and map[curr]+1 >= map[(x,y+1)]:
      if ((x,y+1) in visited and visited[(x,y+1)] > nextCount) or (x,y+1) not in visited:
        visited[(x,y+1)] = nextCount
        next((x,y+1), nextCount, map, target, visited)
    return

  S = None
  E = None
  map = {}
  for y,line in enumerate(LINES):
    for x,c in enumerate(line):
      map[(x,y)] = ord(c) - ord('a')
      if c == 'S':
        S = (x,y)
        map[(x,y)] = ord('a') - ord('a')
      if c == 'E':
        E = (x,y)
        map[(x,y)] = ord('z') - ord('a')

  visited = {}
  next(S, 0, map, E, visited)
  print('Answer 1: ', min(SOLUTION))


# 2. What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
# ------------------------------------------------------------------------------
def problem2():
  SOLUTION = []
  def next(curr, count, map, visited):
    if map[curr] == 0:
      SOLUTION.append(count)
      return

    (x,y) = curr
    nextCount = count + 1

    if x-1 >= 0 and map[curr]-map[(x-1,y)] <= 1:
      if ((x-1,y) in visited and visited[(x-1,y)] > nextCount) or (x-1,y) not in visited:
        visited[(x-1,y)] = nextCount
        next((x-1,y), nextCount, map, visited)
    if y-1 >= 0 and map[curr]-map[(x,y-1)] <= 1:
      if ((x,y-1) in visited and visited[(x,y-1)] > nextCount) or (x,y-1) not in visited:
        visited[(x,y-1)] = nextCount
        next((x,y-1), nextCount, map, visited)
    if x+1 < MAX_X and map[curr]-map[(x+1,y)] <= 1:
      if ((x+1,y) in visited and visited[(x+1,y)] > nextCount) or (x+1,y) not in visited:
        visited[(x+1,y)] = nextCount
        next((x+1,y), nextCount, map, visited)
    if y+1 < MAX_Y and map[curr]-map[(x,y+1)] <= 1:
      if ((x,y+1) in visited and visited[(x,y+1)] > nextCount) or (x,y+1) not in visited:
        visited[(x,y+1)] = nextCount
        next((x,y+1), nextCount, map, visited)
    return

  E = None
  map = {}
  visited = {}
  for y,line in enumerate(LINES):
    for x,c in enumerate(line):
      map[(x,y)] = ord(c) - ord('a')
      if c == 'S':
        map[(x,y)] = ord('a') - ord('a')
      if c == 'E':
        E = (x,y)
        map[(x,y)] = ord('z') - ord('a')

  next(E, 0, map, visited)
  print('Answer 2: ', min(SOLUTION))


# ------------------------------------------------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
