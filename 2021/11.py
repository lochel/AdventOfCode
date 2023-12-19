#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.parseLines(aoc.LINES, lambda line : [int(x) for x in list(line)])

  answer = 0
  for step in range(100):
    for (x, y) in aoc.Grid(lines):
      lines[y][x] += 1

    flash = True
    while flash:
      flash = False
      for (x, y) in aoc.Grid(lines):
        if lines[y][x] > 9:
          flash = True
          lines[y][x] = 0
          answer += 1
          for (a, b) in aoc.get_neighbors(x, y, True, True):
            if lines[b][a] > 0:
              lines[b][a] += 1

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.parseLines(aoc.LINES, lambda line : [int(x) for x in list(line)])

  answer = 0
  all_flash = False
  while not all_flash:
    answer += 1

    for (x, y) in aoc.Grid(lines):
      lines[y][x] += 1

    flash = True
    while flash:
      flash = False
      for (x, y) in aoc.Grid(lines):
        if lines[y][x] > 9:
          flash = True
          lines[y][x] = 0
          for (a, b) in aoc.get_neighbors(x, y, True, True):
            if lines[b][a] > 0:
              lines[b][a] += 1

    all_flash = max([max(x) for x in lines]) == 0

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
