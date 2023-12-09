#!../.env/bin/python3

import aoc

LINES = aoc.parseLines(aoc.LINES, lambda line : line.split(' '))

# 1.
# ----------------------------------------
x, z, aim = 0, 0, 0
for [cmd, value] in LINES:
  value = int(value)
  if cmd == 'forward':
    x += value
    z += aim*value
  elif cmd == 'down':
    z += value
  elif cmd == 'up':
    z -= value
  else:
    print(cmd, value)
    exit(0)
print(f'Answer 1: {x*z}')

# 2.
# ----------------------------------------
x, z, aim = 0, 0, 0
for [cmd, value] in LINES:
  value = int(value)
  if cmd == 'forward':
    x += value
    z += aim*value
  elif cmd == 'down':
    aim += value
  elif cmd == 'up':
    aim -= value
  else:
    print(cmd, value)
    exit(0)
print(f'Answer 2: {x*z}')
