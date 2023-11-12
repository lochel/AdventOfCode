#!../.env/bin/python3

import aoc

aoc.parseLines(int)

# 1.
# ----------------------------------------
def problem1():
  answer = 0
  old = aoc.LINES[0]
  for x in aoc.LINES:
    if x > old:
      answer += 1
    old = x
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = 0
  old = sum(aoc.LINES[0:3])
  for x in range(3, aoc.N+1):
    y = sum(aoc.LINES[x-3:x])
    if y > old:
      answer += 1
    old = y
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
