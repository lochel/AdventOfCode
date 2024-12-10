#!../.env/bin/python3

import aoc

def getScore(grid, x, y):
  score = []
  height = int(grid[y][x])

  if height == 9:
    return [(x,y)]

  for x2,y2 in aoc.get_neighbors(x, y, False, True):
    if int(grid[y2][x2]) == height+1:
      score += getScore(grid, x2, y2)

  return score

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  answer = 0
  for x,y in aoc.Grid(lines):
    if lines[y][x] == '0':
      answer += len(set(getScore(lines, x, y)))

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  answer = 0
  for x,y in aoc.Grid(lines):
    if lines[y][x] == '0':
      answer += len(getScore(lines, x, y))

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
