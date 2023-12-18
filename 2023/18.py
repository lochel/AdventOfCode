#!../.env/bin/python3

import aoc
from shapely.geometry import Polygon

LINES = aoc.parseLines(aoc.LINES, lambda line: line.split())

# 1.
# ----------------------------------------
def problem1():
  x, y = 0, 0
  points = []
  circumference = 0
  for dir, dist, _ in LINES:
    dist = int(dist)

    if dir == 'D':
      y += dist
    elif dir == 'U':
      y -= dist
    elif dir == 'L':
      x -= dist
    elif dir == 'R':
      x += dist

    points.append((x, y))
    circumference += dist

  answer = int(Polygon(points).area + circumference/2 + 1)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  x, y = 0, 0
  points = []
  circumference = 0
  for _, _, color in LINES:
    dist = int(color[2:-2], 16)
    dir = int(color[-2])

    if dir == 1:
      y += dist
    elif dir == 3:
      y -= dist
    elif dir == 2:
      x -= dist
    elif dir == 0:
      x += dist

    circumference += dist
    points.append((x, y))

  answer = int(Polygon(points).area + circumference/2 + 1)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
