#!../.env/bin/python3

import math

import aoc

# 1.
# ----------------------------------------
def problem1():
  LINES = aoc.parseLines(aoc.LINES, lambda line: line.split(':')[1].strip())
  LINES = aoc.parseLines(LINES, lambda line: [int(x) for x in line.split()])
  TIME = LINES[0]
  DIST = LINES[1]

  ways_to_win = []
  for t, d in zip(TIME, DIST):
    count = 0
    for i in range(t):
      if (t-i)*i > d:
        count += 1
    ways_to_win.append(count)

  answer = math.prod(ways_to_win)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  LINES = aoc.replaceLines(aoc.LINES, ' ')
  LINES = aoc.parseLines(LINES, lambda line: int(line.split(':')[1]))
  TIME = LINES[0]
  DIST = LINES[1]

  start = 0
  for i in range(TIME):
    if (TIME-i)*i > DIST:
      start = i
      break

  end = TIME
  for i in range(TIME, 0, -1):
    if (TIME-i)*i > DIST:
      end = i
      break

  answer = end-start+1
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
