#!../.env/bin/python3

from itertools import combinations

from z3 import Real, Solver, sat

import aoc

def line_intersection(line1, line2):
  xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
  ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

  def det(a, b):
      return a[0] * b[1] - a[1] * b[0]

  div = det(xdiff, ydiff)
  if div == 0:
      raise Exception('lines do not intersect')

  d = (det(*line1), det(*line2))
  x = det(d, xdiff) / div
  y = det(d, ydiff) / div
  return x, y

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.replaceLines(lines, ',')
  lines = aoc.replaceLines(lines, '@ ')
  lines = aoc.parseLines(lines, lambda line : [int(x) for x in line.split()])

  answer = 0
  for A, B in combinations(lines, 2):
    (x1, y1, z1, dx1, dy1, dz1) = A
    (x2, y2, z2, dx2, dy2, dz2) = B
    PA = (x1, y1)
    PA2 = (x1+dx1, y1+dy1)

    PB = (x2, y2)
    PB2 = (x2+dx2, y2+dy2)

    try:
      x, y = line_intersection((PA, PA2), (PB, PB2))

      t1 = (x-x1)/dx1 if dx1 != 0 else (y-y1)/dy1
      t2 = (x-x2)/dx2 if dx2 != 0 else (y-y2)/dy2

      if 200000000000000 <=x <= 400000000000000 and 200000000000000 <= y <= 400000000000000 and t1 > 0 and t2 > 0:
         answer += 1
    except Exception:
       pass

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.replaceLines(lines, ',')
  lines = aoc.replaceLines(lines, '@ ')
  lines = aoc.parseLines(lines, lambda line : [int(x) for x in line.split()])

  s = Solver()
  for i,(x,y,z,dx,dy,dz) in enumerate(lines):
      s.add(Real('Px') + Real(f't{i}')*Real('Pdx') == x + Real(f't{i}')*dx)
      s.add(Real('Py') + Real(f't{i}')*Real('Pdy') == y + Real(f't{i}')*dy)
      s.add(Real('Pz') + Real(f't{i}')*Real('Pdz') == z + Real(f't{i}')*dz)

  if s.check() == sat:
      m = s.model()
      answer = m.eval(Real('Px') + Real('Py') + Real('Pz'))
  else:
    answer = None

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
