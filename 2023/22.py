#!../.env/bin/python3

from collections import defaultdict, deque

import aoc

BRICKS = []
for i,line in enumerate(aoc.LINES):
  A, B = line.split('~')
  (x1, y1, z1) = A.split(',')
  (x2, y2, z2) = B.split(',')
  BRICKS.append((int(x1), int(y1), int(z1), int(x2), int(y2), int(z2), i+1))

ZMAX = max([max(x[2], x[5]) for x in BRICKS]) + 1
BRICKS.sort(key=lambda x : x[2]*ZMAX+x[5])

XMAX, YMAX = max([max(x[0], x[3]) for x in BRICKS]), max([max(x[1], x[4]) for x in BRICKS])

TOWER = {}
for x in range(XMAX+1):
  for y in range(YMAX+1):
    TOWER[(x, y, 0)] = 0

SUPPORTING = defaultdict(set)
for (x1, y1, z1, x2, y2, z2, brickID) in BRICKS:
  if x1 != x2:
    assert y1 == y2
    assert z1 == z2
    cubes = [(x, y1, z1) for x in range(x1, x2+1)]
  elif y1 != y2:
    assert x1 == x2
    assert z1 == z2
    cubes = [(x1, y, z1) for y in range(y1, y2+1)]
  else:
    assert x1 == x2
    assert y1 == y2
    cubes = [(x1, y1, z) for z in range(z1, z2+1)]

  falling_height = 0
  while True:
    falling_height += 1
    if any([(x,y,z-falling_height) in TOWER for (x,y,z) in cubes]):
      for (x,y,z) in cubes:
        if (x,y,z-falling_height) in TOWER:
          SUPPORTING[TOWER[(x,y,z-falling_height)]].add(brickID)
      falling_height -= 1
      break

  for (x,y,z) in cubes:
    TOWER[(x,y,z-falling_height)] = brickID

# 1.
# ----------------------------------------
def problem1():
  disintegrate = set()
  for (x1, y1, z1, x2, y2, z2, brickID) in BRICKS:
    visited = [False for x in range(aoc.N+1)]
    visited[brickID] = True

    Q = deque([0])
    while Q:
      x = Q.pop()
      if visited[x]:
        continue
      visited[x] = True
      for y in SUPPORTING[x]:
        Q.append(y)

    if all(visited):
      disintegrate.add(brickID)

  answer = len(disintegrate)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = 0
  for (x1, y1, z1, x2, y2, z2, brickID) in BRICKS:
    visited = [0 for x in range(aoc.N+1)]
    visited[brickID] = 1

    Q = deque([0])
    while Q:
      x = Q.pop()
      if visited[x] == 1:
        continue
      visited[x] = 1
      for y in SUPPORTING[x]:
        Q.append(y)

    answer += len(visited)-sum(visited)

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
