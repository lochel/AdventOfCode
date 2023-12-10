#!../.env/bin/python3

from collections import deque
import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.parseLines(aoc.LINES, lambda line : list(line))

  START = None
  for (x, y) in aoc.Grid(lines):
    if lines[y][x] == 'S':
      START = (x, y)
      break

  pX, pY = START
  points = [START]
  while True:
    #print("Current", pX, pY, lines[pY][pX])
    for (x, y) in aoc.get_neighbors(pX, pY, diagonals=False):
      if (x, y) in points:
        continue

      if x > pX and lines[pY][pX] in '-FLS' and lines[y][x] in '-7JS':
        pX = x
        break
      if x < pX and lines[pY][pX] in '-7JS' and lines[y][x] in '-FLS':
        pX = x
        break
      if y < pY and lines[pY][pX] in '|LJS' and lines[y][x] in '|F7S':
        pY = y
        break
      if y > pY and lines[pY][pX] in '|F7S' and lines[y][x] in '|LJS':
        pY = y
        break

    if (pX, pY) in points:
      break

    points.append((pX, pY))

  answer = len(points)//2
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.parseLines(aoc.LINES, lambda line : list(line))

  START = None
  for (x, y) in aoc.Grid(lines):
    if lines[y][x] == 'S':
      START = (x, y)
      break

  pX, pY = START
  points = [START]
  while True:
    for (x, y) in aoc.get_neighbors(pX, pY, diagonals=False):
      if (x, y) in points:
        continue

      if x > pX and lines[pY][pX] in '-FLS' and lines[y][x] in '-7JS':
        pX = x
        break
      if x < pX and lines[pY][pX] in '-7JS' and lines[y][x] in '-FLS':
        pX = x
        break
      if y < pY and lines[pY][pX] in '|LJS' and lines[y][x] in '|F7S':
        pY = y
        break
      if y > pY and lines[pY][pX] in '|F7S' and lines[y][x] in '|LJS':
        pY = y
        break

    if (pX, pY) in points:
      break

    points.append((pX, pY))

  # Remove noise
  for (x,y) in aoc.Grid(lines):
    if (x, y) not in points:
      lines[y][x] = ' '

  # Scale up the map
  map = []
  for y in range(aoc.N*3):
    map.append(['.']*3*aoc.M)

  for (x, y) in points:
    map[3*y+1][3*x+1] = lines[y][x]

    #     012
    # +0: .S.
    # +1: SSS
    # +2: .S.
    if lines[y][x] == 'S':
      map[3*y+1][3*x+0] = 'S'
      map[3*y+1][3*x+2] = 'S'
      map[3*y+0][3*x+1] = 'S'
      map[3*y+2][3*x+1] = 'S'

    #     012
    # +0: ...
    # +1: ---
    # +2: ...
    if lines[y][x] == '-':
      map[3*y+1][3*x+0] = '-'
      map[3*y+1][3*x+2] = '-'

    #     012
    # +0: .|.
    # +1: .|.
    # +2: .|.
    if lines[y][x] == '|':
      map[3*y+0][3*x+1] = '|'
      map[3*y+2][3*x+1] = '|'

    #     012
    # +0: .J.
    # +1: JJ.
    # +2: ...
    if lines[y][x] == 'J':
      map[3*y+0][3*x+1] = 'J'
      map[3*y+1][3*x+0] = 'J'

    #     012
    # +0: ...
    # +1: 77.
    # +2: .7.
    if lines[y][x] == '7':
      map[3*y+1][3*x+0] = '7'
      map[3*y+2][3*x+1] = '7'

    #     012
    # +0: .L.
    # +1: .LL
    # +2: ...
    if lines[y][x] == 'L':
      map[3*y+0][3*x+1] = 'L'
      map[3*y+1][3*x+2] = 'L'

    #     012
    # +0: ...
    # +1: .FF
    # +2: .F.
    if lines[y][x] == 'F':
      map[3*y+1][3*x+2] = 'F'
      map[3*y+2][3*x+1] = 'F'

  # Print map
  #print()
  #for line in map:
  #  print(''.join(line))

  Q = deque()

  # The border is always outside (due to the upscaling)
  for x in range(aoc.M*3):
    Q.append((x, 0))
    Q.append((x, 3*aoc.N-1))
  for y in range(aoc.N*3):
    Q.append((0, y))
    Q.append((3*aoc.M-1, y))

  # Remove all fields that are connected to the outside
  while Q:
    (x, y) = Q.pop()
    map[y][x] = ' '

    for (nx, ny) in aoc.get_neighbors(x, y, diagonals=False, maxX = 3*aoc.M, maxY = 3*aoc.N):
      if map[ny][nx] == '.':
        Q.append((nx, ny))

  # Count the remaining fields
  answer = 0
  for (x, y) in aoc.Grid(lines):
    if map[3*y+1][3*x+1] == '.':
      answer += 1

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
