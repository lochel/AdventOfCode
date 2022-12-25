#!../.env/bin/python3

import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else '03.in'
LINES = [line.strip() for line in open(input_file)]

# 1. How many houses receive at least one present?
# ----------------------------------------
def problem1():
  x, y = 0, 0
  houses = set([(x, y)])
  for dir in LINES[0]:
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
  for idx,dir in enumerate(LINES[0]):
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
