#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  answer = 0

  y = 0
  while y < aoc.M:
    x = 0
    while x+3 < aoc.N:
      if lines[y][x] == 'X' and lines[y][x+1] == 'M' and lines[y][x+2] == 'A' and lines[y][x+3] == 'S':
        answer += 1
      if lines[y][x] == 'S' and lines[y][x+1] == 'A' and lines[y][x+2] == 'M' and lines[y][x+3] == 'X':
        answer += 1
      x += 1
    y += 1

  y = 0
  while y+3 < aoc.M:
    x = 0
    while x < aoc.N:
      if lines[y][x] == 'X' and lines[y+1][x] == 'M' and lines[y+2][x] == 'A' and lines[y+3][x] == 'S':
        answer += 1
      if lines[y][x] == 'S' and lines[y+1][x] == 'A' and lines[y+2][x] == 'M' and lines[y+3][x] == 'X':
        answer += 1
      x += 1
    y += 1

  y = 0
  while y+3 < aoc.M:
    x = 0
    while x+3 < aoc.N:
      if lines[y][x] == 'X' and lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S':
        answer += 1
      if lines[y][x] == 'S' and lines[y+1][x+1] == 'A' and lines[y+2][x+2] == 'M' and lines[y+3][x+3] == 'X':
        answer += 1
      x += 1
    y += 1

  y = 0
  while y+3 < aoc.M:
    x = 3
    while x < aoc.N:
      if lines[y][x] == 'X' and lines[y+1][x-1] == 'M' and lines[y+2][x-2] == 'A' and lines[y+3][x-3] == 'S':
        answer += 1
      if lines[y][x] == 'S' and lines[y+1][x-1] == 'A' and lines[y+2][x-2] == 'M' and lines[y+3][x-3] == 'X':
        answer += 1
      x += 1
    y += 1

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  answer = 0

  y = 1
  while y+1 < aoc.M:
    x = 1
    while x+1 < aoc.N:
      if lines[y][x] == 'A' :
        if lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S' and lines[y+1][x-1] == 'M' and lines[y-1][x+1] == 'S':
          answer += 1
        if lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S' and lines[y+1][x-1] == 'S' and lines[y-1][x+1] == 'M':
          answer += 1
        if lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M' and lines[y+1][x-1] == 'M' and lines[y-1][x+1] == 'S':
          answer += 1
        if lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M' and lines[y+1][x-1] == 'S' and lines[y-1][x+1] == 'M':
          answer += 1
      x += 1
    y += 1

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
