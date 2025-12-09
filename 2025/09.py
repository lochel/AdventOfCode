#!../.env/bin/python3

import aoc
from shapely import Polygon

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  tiles = aoc.parseLines(lines, lambda x: tuple(int(n) for n in x.split(',')))

  answer = 0
  for i, (x, y) in enumerate(tiles):
    for j, (xx, yy) in enumerate(tiles):
      if abs(x - xx + 1) * abs(y - yy + 1) > answer:
        answer = abs(x - xx + 1) * abs(y - yy + 1)

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  #1467543012 too low
  #1476517912 too low
  #1636493624 too high

  lines = aoc.LINES
  tiles = aoc.parseLines(lines, lambda x: tuple(int(n) for n in x.split(',')))

  polygon = Polygon(tiles)

  answer = 0
  for x1, y1 in tiles:
    for x2, y2 in tiles:
      x_min, y_min = min(x1,x2), min(y1,y2)
      x_max, y_max = max(x1,x2), max(y1,y2)
      rectangle = Polygon([(x_min,y_min),(x_max,y_min),(x_max,y_max),(x_min,y_max)])
      if rectangle.within(polygon):
        area = (y_max - y_min + 1) * (x_max - x_min + 1)
        if area > answer:
          answer = area

  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()