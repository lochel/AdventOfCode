#!../.env/bin/python3

import sys

import aoc

sys.setrecursionlimit(10000)

Q = set()
TILES = set()
GRID = aoc.parseLines(aoc.LINES, lambda line : list(line))

def step(x, y, xdir, ydir):
  if not (0 <= x < aoc.M and 0 <= y < aoc.N):
    return

  if (x, y, xdir, ydir) in Q:
    return
  else:
    Q.add((x, y, xdir, ydir))
    TILES.add((x, y))

  if GRID[y][x] == '.' or (GRID[y][x] == '-' and ydir == 0)  or (GRID[y][x] == '|' and xdir == 0):
    step(x+xdir, y+ydir, xdir, ydir)
  elif GRID[y][x] == '-':
    step(x+1, y, 1, 0)
    step(x-1, y, -1, 0)
  elif GRID[y][x] == '|':
    step(x, y+1, 0, 1)
    step(x, y-1, 0, -1)
  elif GRID[y][x] == '\\':
    step(x+ydir, y+xdir, ydir, xdir)
  elif GRID[y][x] == '/':
    step(x-ydir, y-xdir, -ydir, -xdir)

# 1.
# ----------------------------------------
def problem1():
  step(0, 0, 1, 0)
  answer = len(TILES)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  num_tiles = []
  for x in range(aoc.M):
    Q.clear()
    TILES.clear()
    step(x, 0, 0, 1)
    num_tiles.append(len(TILES))

    Q.clear()
    TILES.clear()
    step(x, aoc.N-1, 0, -1)
    num_tiles.append(len(TILES))

  for y in range(aoc.N):
    Q.clear()
    TILES.clear()
    step(0, y, 1, 0)
    num_tiles.append(len(TILES))

    Q.clear()
    TILES.clear()
    step(aoc.M-1, y, -1, 0)
    num_tiles.append(len(TILES))

  answer = max(num_tiles)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
