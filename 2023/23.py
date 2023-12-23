#!../.env/bin/python3

import copy
import sys
from collections import deque

import aoc

sys.setrecursionlimit(10000)

# 1.
# ----------------------------------------
def problem1():
  map = aoc.parseLines(aoc.LINES, lambda line : list(line))

  for i in range(aoc.M):
    if map[0][i] == '.':
      start = (i, 0)
    if map[aoc.N-1][i] == '.':
      stop = (i, aoc.N-1)

  def step(pos, stop, path):
    if pos == stop:
      return len(path)

    path.add(pos)

    x, y = pos

    if map[y][x] == '>' and (x+1,y) not in path:
      length = step((x+1, y), stop, path)
    elif map[y][x] == 'v' and (x,y+1) not in path:
      length = step((x, y+1), stop, path)
    elif map[y][x] == '.':
      neighbors = [(xx, yy) for (xx, yy) in aoc.get_neighbors(x, y, diagonals=False, check_bounds=True) if (xx, yy) not in path and map[yy][xx] != '#']
      length = max([step(neighbor, stop, path) for neighbor in neighbors])
    else:
      length = 0

    path.remove(pos)
    return length

  answer = step(start, stop, set())
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  map = aoc.parseLines(aoc.LINES, lambda line : list(line))

  def is_intersection(x, y):
    neighbors = [(xx, yy) for (xx, yy) in aoc.get_neighbors(x, y, diagonals=False, check_bounds=True) if map[yy][xx] != '#']
    return len(neighbors) > 2

  def get_intersections(x, y, intersections, step=0, visited=None):
    if not visited:
      visited = set()

    visited.add((x, y))
    neighbors = [(xx, yy, step+1) for (xx, yy) in aoc.get_neighbors(x, y, diagonals=False, check_bounds=True) if (xx,yy) not in visited and map[yy][xx] != '#']

    nodes = []
    for (x, y, z) in neighbors:
      if (x, y) in intersections:
        nodes.append((x, y, z))
      else:
        nodes += get_intersections(x, y, intersections, step+1, visited)
    return nodes

  for i in range(aoc.M):
    if map[0][i] == '.':
      start = (i, 0)
    if map[aoc.N-1][i] == '.':
      stop = (i, aoc.N-1)

  intersection_positions = set([start, stop])
  for (x, y) in aoc.Grid(map):
    if is_intersection(x, y):
      intersection_positions.add((x, y))

  intersections = {}
  intersections[start] = get_intersections(start[0], start[1], intersection_positions)
  intersections[stop] = get_intersections(stop[0], stop[1], intersection_positions)
  for (x, y) in aoc.Grid(map):
    if is_intersection(x, y):
      intersections[(x, y)] = get_intersections(x, y, intersection_positions)

  def step(pos, stop, path=None, length=0):
    if pos == stop:
      return length

    if not path:
      path = set()

    path.add(pos)

    res = 0
    for (x, y, z) in intersections[pos]:
      if (x, y) not in path:
        res = max(res, step((x, y), stop, path, length+z))

    path.remove(pos)
    return res

  answer = step(start, stop)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
