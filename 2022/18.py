#!../.env/bin/python3

from aoc import LINES, N
LINES = [line.split(',') for line in LINES]

LAVA = set()
for x,y,z in LINES:
  x,y,z = int(x),int(y),int(z)
  LAVA.add((x,y,z))

bx = (min([int(x) for x,_,_ in LINES]), max([int(x) for x,_,_ in LINES]))
by = (min([int(y) for _,y,_ in LINES]), max([int(y) for _,y,_ in LINES]))
bz = (min([int(z) for _,_,z in LINES]), max([int(z) for _,_,z in LINES]))

INSIDE = set()
OUTSIDE = set()

def isOutside(x, y, z):
  global INSIDE, OUTSIDE
  Q = [(x,y,z)]
  P = set()
  while Q:
    p = Q.pop()
    if p in P:
      continue
    if p in LAVA:
      continue

    P.add(p)
    if p in OUTSIDE:
      OUTSIDE = OUTSIDE.union(P)
      return True
    if p in INSIDE:
      INSIDE = INSIDE.union(P)
      return False

    x,y,z = p
    if not (bx[0] <= x <= bx[1] and by[0] <= y <= by[1] and bz[0] <= z <= bz[1]):
      OUTSIDE = OUTSIDE.union(P)
      return True

    for d in [-1, 1]:
      Q.append((x+d,y,z))
      Q.append((x,y+d,z))
      Q.append((x,y,z+d))

  INSIDE = INSIDE.union(P)
  return False


# 1. What is the surface area of your scanned lava droplet?
# ----------------------------------------
def problem1():
  surface = 0
  for x,y,z in LAVA:
    for d in [-1, 1]:
      if (x+d,y,z) not in LAVA:
        surface += 1
      if (x,y+d,z) not in LAVA:
        surface += 1
      if (x,y,z+d) not in LAVA:
        surface += 1

  print(f'Answer 1: {surface}')


# 2. What is the exterior surface area of your scanned lava droplet?
# ----------------------------------------
def problem2():
  surface = 0
  for x,y,z in LAVA:
    for d in [-1, 1]:
      if isOutside(x+d,y,z):
        surface += 1
      if isOutside(x,y+d,z):
        surface += 1
      if isOutside(x,y,z+d):
        surface += 1

  print(f'Answer 2: {surface}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
