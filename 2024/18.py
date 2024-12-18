#!../.env/bin/python3

from collections import deque

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split(','))
  lines = [[int(x) for x in line] for line in lines]

  X, Y = 70, 70

  map = [['.' for _ in range(X+1)] for _ in range(Y+1)]

  for idx,line in enumerate(lines):
    x,y = line
    map[y][x] = '#'

    if idx == 1023:
      break

  Q = deque([(0, 0)])
  map[0][0] = 0
  while Q:
    x, y = Q.popleft()

    if x == X and y == Y:
      answer = map[y][x]
      break

    neighbors = aoc.get_neighbors(x, y, False, True, X+1, Y+1)
    for nx, ny in neighbors:
      if map[ny][nx] == '.':
        map[ny][nx] = map[y][x] + 1
        Q.append((nx, ny))
  #aoc.printGrid(map, delimiter='')
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split(','))
  lines = [[int(x) for x in line] for line in lines]

  X, Y = 70, 70

  map = set()

  for idx,line in enumerate(lines):
    x,y = line
    map.add((x,y))

    if idx < 1024:
      continue

    Q = deque([(0, 0)])
    SEEN = set()
    SEEN.add((0,0))
    answer = f'{x},{y}'

    while Q:
      x, y = Q.popleft()

      if x == X and y == Y:
        answer = None
        break

      neighbors = aoc.get_neighbors(x, y, False, True, X+1, Y+1)
      for nx, ny in neighbors:
        if (nx,ny) not in map and (nx,ny) not in SEEN:
          Q.append((nx, ny))
          SEEN.add((nx,ny))
    if answer:
      break

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
