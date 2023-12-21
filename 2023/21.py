#!../.env/bin/python3

from collections import deque

import aoc

# 1.
# ----------------------------------------
def problem1():
  map = aoc.parseLines(aoc.LINES, lambda line : list(line))

  for x,y in aoc.Grid(map):
    if map[y][x] == 'S':
      pos = (x, y)

  Q = deque()
  end = set([pos])
  for _ in range(64):
    Q = deque(end)
    end = set()

    while Q:
      x, y = Q.pop()
      for (xx, yy) in aoc.get_neighbors(x, y, False, True):
        if map[yy][xx] in '.S':
          end.add((xx, yy))

  print(f'Answer 1: {len(end)}')

# 2.
# ----------------------------------------
def problem2():
  map = aoc.parseLines(aoc.LINES, lambda line : list(line))

  for x,y in aoc.Grid(map):
    if map[y][x] == 'S':
      pos = (x, y)

  Q = deque()
  end = set([pos])

  countEven, countOdd = None, None
  count = {}
  step = 0
  while True:
    step += 1
    Q = deque(end)
    end = set()

    while Q:
      x, y = Q.pop()
      for (xx, yy) in aoc.get_neighbors(x, y, False, True):
        if map[yy][xx] in '.S':
          end.add((xx, yy))

    count[step] = len(end)

    if count[step] in [countEven, countOdd] and count[step-1] in [countEven, countOdd]:
      break

    if step % 2 == 0:
      countEven = len(end)
    else:
      countOdd = len(end)

  n = (26501365 - aoc.N//2) // aoc.N

  cornersEven = countEven - count[64]
  cornersOdd  = countOdd - count[65]

  answer = (n+1)**2 * countOdd + n**2 * countEven - (n+1) * cornersOdd + n * cornersEven
  print(f'Answer 2: {answer}')

  #       XXX
  #       XXX
  #       XXX
  #    XXX   XXX
  #    XXX   XXX
  #    XXX   XXX
  # XXX         XXX
  # XXX    S    XXX
  # XXX         XXX
  #    XXX   XXX
  #    XXX   XXX
  #    XXX   XXX
  #       XXX
  #       XXX
  #       XXX

  # 631357595415612: That's not the right answer; your answer is too low.
  # 631357543626812: That's not the right answer; your answer is too low.
  # 631357543626746: That's not the right answer; your answer is too low.
  # 631357595415546: That's not the right answer; your answer is too low.

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
