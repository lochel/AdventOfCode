#!../.env/bin/python3

import sys

import aoc

sys.setrecursionlimit(10000)

GRID = aoc.parseLines(aoc.LINES, lambda line : [int(x) for x in list(line)])

solution = []
CACHE = {}

def step(x, y, xdir, ydir, count, heat, part2):
  if not (0<=x<aoc.M and 0<=y<aoc.N):
    return

  new_heat = heat + GRID[y][x]

  state = (x, y, xdir, ydir, count)
  if state in CACHE and new_heat >= CACHE[state]:
    return

  CACHE[state] = new_heat

  if solution and new_heat >= min(solution):
    return

  max_count = 9 if part2 else 2
  min_count = 3 if part2 else 0

  if x == aoc.M-1 and y == aoc.N-1 and count >= min_count:
    print("Reached goal", new_heat)
    solution.append(new_heat)
    return

  if count < max_count:
    step(x+xdir, y+ydir, xdir, ydir, count+1, new_heat, part2)
  if xdir == 0 and count >= min_count:
    step(x+1, y, +1, 0, 0, new_heat, part2)
    step(x-1, y, -1, 0, 0, new_heat, part2)
  if ydir == 0 and count >= min_count:
    step(x, y+1, 0, +1, 0, new_heat, part2)
    step(x, y-1, 0, -1, 0, new_heat, part2)

# 1.
# ----------------------------------------
def problem1():
  solution.clear()
  solution.append(800)
  CACHE.clear()
  step(0, 0, 1, 0, 0, -GRID[0][0], False)
  step(0, 0, 0, 1, 0, -GRID[0][0], False)
  answer = min(solution)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  solution.clear()
  solution.append(1000)
  CACHE.clear()
  step(0, 0, 1, 0, 0, -GRID[0][0], True)
  step(0, 0, 0, 1, 0, -GRID[0][0], True)
  answer = min(solution)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
