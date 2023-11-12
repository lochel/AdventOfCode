#!../.env/bin/python3

import aoc

LINES = aoc.parseLines(lambda line : line.split(','))

# 1. In how many assignment pairs does one range fully contain the other?
# --------------------------------------
def problem1():
  answer = 0
  for [a, b] in LINES:
    a = [int(i) for i in a.split('-')]
    b = [int(i) for i in b.split('-')]
    if a[0] <= b[0] and a[1] >= b[1]:
      answer += 1
    elif a[0] >= b[0] and a[1] <= b[1]:
      answer += 1
  return answer


# 2. In how many assignment pairs do the ranges overlap?
# --------------------------------------
def problem2():
  answer = 0
  for [a, b] in LINES:
    a = [int(i) for i in a.split('-')]
    b = [int(i) for i in b.split('-')]
    if a[0] <= b[0] <= a[1]:
      answer += 1
    elif a[0] <= b[1] <= a[1]:
      answer += 1
    elif b[0] <= a[0] <= b[1]:
      answer += 1
    elif b[0] <= a[1] <= b[1]:
      answer += 1
  return answer


# --------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {problem1()}')
  print(f'Answer 2: {problem2()}')
