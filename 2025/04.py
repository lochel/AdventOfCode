#!../.env/bin/python3

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.parseLines(aoc.LINES, list)

  answer = 0
  for (x, y) in aoc.Grid(lines):
    if lines[y][x] == '.':
      continue

    if sum([1 for (nx, ny) in aoc.get_neighbors(x, y, diagonals=True) if lines[ny][nx] != '.']) < 4:
      answer += 1

  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  lines = aoc.parseLines(aoc.LINES, list)

  answer = 0
  done = False
  while not done:
    done = True

    for (x, y) in aoc.Grid(lines):
      if lines[y][x] == '.':
        continue

      if sum([1 for (nx, ny) in aoc.get_neighbors(x, y, diagonals=True) if lines[ny][nx] != '.']) < 4:
        lines[y][x] = '.'
        answer += 1
        done = False

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
