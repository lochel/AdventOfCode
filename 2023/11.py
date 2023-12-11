#!../.env/bin/python3

from itertools import combinations

import aoc

LINES = aoc.parseLines(aoc.LINES, lambda line: list(line))

def get_answer(d):
  galaxies = []
  for (x, y) in aoc.Grid(LINES):
    if LINES[y][x] == '#':
      galaxies.append((x, y))

  map = aoc.makeGrid(aoc.M, aoc.N, 1)

  for x in range(aoc.M):
    if x not in [g[0] for g in galaxies]:
      for y in range(aoc.N):
        map[y][x] = d

  for y in range(aoc.N):
    if y not in [g[1] for g in galaxies]:
      for x in range(aoc.M):
        map[y][x] = d

  #aoc.printGrid(map)

  answer = 0
  for (x1, y1), (x2, y2) in combinations(galaxies, 2):
    for x in range(min(x1, x2), max(x1, x2)):
      answer += map[y2][x]
    for y in range(min(y1, y2), max(y1, y2)):
      answer += map[y][x2]
  return answer

# ----------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {get_answer(2)}')
  print(f'Answer 2: {get_answer(1000000)}')
