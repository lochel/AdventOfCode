#!../.env/bin/python3

import math
import aoc

LR = aoc.LINES[0]

DATA = aoc.LINES[2:]
DATA = aoc.replaceLines(DATA, '= (')
DATA = aoc.replaceLines(DATA, ',')
DATA = aoc.replaceLines(DATA, ')')
DATA = aoc.parseLines(DATA, lambda line : line.split())

MAP = {}
START = []
for a,b,c in DATA:
  MAP[a] = (b, c)
  if a[-1] == 'A':
    START.append(a)
# 1.
# ----------------------------------------
def problem1():
  cursor = 0
  answer = 0
  pos = 'AAA'
  while True:
    answer += 1
    dir = LR[cursor]
    (L, R) = MAP[pos]
    if dir == 'L':
      pos = L
    elif dir == 'R':
      pos = R
    else:
      print('Error')
      return

    if pos == 'ZZZ':
      break

    cursor += 1
    cursor = cursor % len(LR)

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  cycles = []
  for pos in START:
    cursor = 0
    steps = 0
    while True:
      steps += 1
      dir = LR[cursor]
      (L, R) = MAP[pos]
      if dir == 'L':
        pos = L
      elif dir == 'R':
        pos = R
      else:
        print('Error')
        return

      if pos[-1] == 'Z':
        # It seems that the offset for all cycles is 0.
        cycles.append(steps)
        break

      cursor += 1
      cursor = cursor % len(LR)

  answer = math.lcm(*cycles)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
