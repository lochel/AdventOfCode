#!../.env/bin/python3

import aoc

# 1. How many houses receive at least one present?
# ----------------------------------------
def problem1():
  x, y = 0, 0
  houses = set([(x, y)])
  for dir in aoc.DATA:
    if dir == '<': x -= 1
    elif dir == '>': x += 1
    elif dir == '^': y -= 1
    elif dir == 'v': y += 1
    else: assert False, dir
    houses.add((x, y))
  print(f'Answer 1: {len(houses)}')

# 2. This year, how many houses receive at least one present?
# ----------------------------------------
def problem2():
  x, y = 0, 0
  a, b = 0, 0
  houses = set([(x, y)])
  for idx,dir in enumerate(aoc.DATA):
    if idx % 2 == 0:
      if dir == '<': x -= 1
      elif dir == '>': x += 1
      elif dir == '^': y -= 1
      elif dir == 'v': y += 1
      else: assert False, dir
      houses.add((x, y))
    else:
      if dir == '<': a -= 1
      elif dir == '>': a += 1
      elif dir == '^': b -= 1
      elif dir == 'v': b += 1
      else: assert False, dir
      houses.add((a, b))
  print(f'Answer 2: {len(houses)}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
