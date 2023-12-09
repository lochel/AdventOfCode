#!../.env/bin/python3

import aoc

LINES = aoc.parseLines(aoc.LINES, lambda line : int(line))

# 1.
# ----------------------------------------
def problem1():
  answer = 0
  old = LINES[0]
  for x in LINES:
    if x > old:
      answer += 1
    old = x
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = 0
  old = sum(LINES[0:3])
  for x in range(3, aoc.N+1):
    y = sum(LINES[x-3:x])
    if y > old:
      answer += 1
    old = y
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
