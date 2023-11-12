#!../.env/bin/python3

import aoc

LINES = aoc.parseLines(lambda line : line.split())


# 1. How many positions does the tail of the rope visit at least once?
# --------------------------------------
def problem1():
  T = 2*[(1, 1)]
  pos = set()
  pos.add(T[1])
  for (action, n_steps) in LINES:
    n_steps = int(n_steps)
    for step in range(n_steps):
      (x, y) = T[0]
      (a, b) = T[1]

      # 1. Move HEAD
      if action == "D":
        y-=1
      elif action == "U":
        y+=1
      elif action == "L":
        x-=1
      elif action == "R":
        x+=1

      # 2. Is TAIL touching?
      if y == b:
        if abs(x-a) > 1:
          a += (x-a)/abs(x-a)
      elif x == a:
        if abs(y-b) > 1:
          b += (y-b)/abs(y-b)
      elif max(abs(x-a), abs(y-b)) > 1:
        a += (x-a)/abs(x-a)
        b += (y-b)/abs(y-b)

      T[0] = (x, y)
      T[1] = (int(a), int(b))
      pos.add(T[1])
  return len(pos)


# 2. How many positions does the tail of the rope visit at least once?
# --------------------------------------
def problem2():
  T = 10*[(1, 1)]
  pos = set()
  pos.add(T[9])
  for (action, n_steps) in LINES:
    n_steps = int(n_steps)
    for step in range(n_steps):
      # 1. Move HEAD
      (x, y) = T[0]
      if action == "D":
        y-=1
      elif action == "U":
        y+=1
      elif action == "L":
        x-=1
      elif action == "R":
        x+=1
      T[0] = (x, y)

      for knot in range(1, 10):
        (x, y) = T[knot-1]
        (a, b) = T[knot]

        # 2. Is TAIL touching?
        if y == b:
          if abs(x-a) > 1:
            a += (x-a)/abs(x-a)
        elif x == a:
          if abs(y-b) > 1:
            b += (y-b)/abs(y-b)
        elif max(abs(x-a), abs(y-b)) > 1:
          a += (x-a)/abs(x-a)
          b += (y-b)/abs(y-b)
        T[knot] = (int(a), int(b))
      pos.add(T[9])
  return len(pos)


# --------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {problem1()}')
  print(f'Answer 2: {problem2()}')
