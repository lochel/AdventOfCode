#!../.env/bin/python3

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : (line[0], int(line[1:])))

  answer = 0
  pos = 50
  for direction, value in lines:
    pos += value if direction == 'R' else -value
    pos %= 100
    if pos == 0:
      answer += 1

  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : (line[0], int(line[1:])))

  answer = 0
  pos = 50
  for direction, value in lines:
    for _ in range(value):
      pos += 1 if direction == 'R' else -1
      pos %= 100
      if pos == 0:
        answer += 1

  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
