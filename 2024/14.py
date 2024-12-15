#!../.env/bin/python3

from math import prod

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  robots = []
  for line in lines:
    [p_,v_] = line.split(' ')
    p_ = p_.split(',')
    p = (int(p_[0][2:]), int(p_[1]))
    v_ = v_.split(',')
    v = (int(v_[0][2:]), int(v_[1]))
    robots.append((p, v))

  XX = 101
  YY = 103
  Q = [0, 0, 0, 0]
  for p,v in robots:
    px,py = p
    for _ in range(100):
      px += v[0]
      py += v[1]

      if px < 0:
        px += XX
      elif px >= XX:
        px -= XX

      if py < 0:
        py += YY
      elif py >= YY:
        py -= YY

    i=''
    if px < XX//2 and py < YY//2:
      Q[0] += 1
      i = '1'
    elif px > XX//2 and py < YY//2:
      Q[1] += 1
      i = '2'
    elif px < XX//2 and py > YY//2:
      Q[2] += 1
      i = '3'
    elif px > XX//2 and py > YY//2:
      Q[3] += 1
      i = '4'

  answer = prod(Q)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  robots = []
  for line in lines:
    [p_,v_] = line.split(' ')
    p_ = p_.split(',')
    p = (int(p_[0][2:]), int(p_[1]))
    v_ = v_.split(',')
    v = (int(v_[0][2:]), int(v_[1]))
    robots.append((p, v))

  XX = 101
  YY = 103
  pos = {}
  for i,(p,v) in enumerate(robots):
    pos[i] = p

  for step in range(100_000):
    for i,(_,v) in enumerate(robots):
      px,py = pos[i]
      px += v[0]
      py += v[1]

      if px < 0:
        px += XX
      elif px >= XX:
        px -= XX

      if py < 0:
        py += YY
      elif py >= YY:
        py -= YY

      pos[i] = (px, py)

    found = False
    for (abx, aby) in pos.values():
      if (abx+1,aby) in pos.values() and (abx+2,aby) in pos.values() and (abx+3,aby) in pos.values() and (abx+4,aby) in pos.values() and (abx+5,aby) in pos.values() and (abx+6,aby) in pos.values() and (abx+7,aby) in pos.values():
        found = True
        break

    if found:
      print(step)
      for j in range(YY):
        for i in range(XX):
          if (i,j) in pos.values():
            print('#', end='')
          else:
            print(' ', end='')
        print()
      answer = step+1
      print(f'Answer 2: {answer}')
      return

  answer = None
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
