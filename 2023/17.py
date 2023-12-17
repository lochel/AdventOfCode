#!../.env/bin/python3

from collections import deque

import aoc

GRID = aoc.parseLines(aoc.LINES, lambda line : [int(x) for x in list(line)])

def step(part2):
  solution = None
  CACHE = {}

  Q = deque([(0, 0, 1, 0, 0, -GRID[0][0]), (0, 0, 0, 1, 0, -GRID[0][0])])

  while Q:
    if not solution: # heuristic to find a solution quickly
      Q = deque(sorted(Q, key=lambda state: state[0] + state[1]))
    (x, y, xdir, ydir, count, heat) = Q.pop()

    if not (0<=x<aoc.M and 0<=y<aoc.N):
      continue

    new_heat = heat + GRID[y][x]

    state = (x, y, xdir, ydir, count)
    if state in CACHE and new_heat >= CACHE[state]:
      continue

    CACHE[state] = new_heat

    if solution and new_heat >= solution:
      continue

    max_count = 9 if part2 else 2
    min_count = 3 if part2 else 0

    if x == aoc.M-1 and y == aoc.N-1 and count >= min_count:
      print(f"Best guess so far: {new_heat}, {len(Q):<10}", end='\r')
      solution = new_heat
      continue

    if xdir == 0 and count >= min_count:
      Q.append((x+1, y, +1, 0, 0, new_heat))
      Q.append((x-1, y, -1, 0, 0, new_heat))
    if ydir == 0 and count >= min_count:
      Q.append((x, y+1, 0, +1, 0, new_heat))
      Q.append((x, y-1, 0, -1, 0, new_heat))
    if count < max_count:
      Q.append((x+xdir, y+ydir, xdir, ydir, count+1, new_heat))

  return solution

# 1.
# ----------------------------------------
def problem1():
  answer = step(False)
  print(f'Answer 1: {answer:<20}')

# 2.
# ----------------------------------------
def problem2():
  answer = step(True)
  print(f'Answer 2: {answer:<20}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
