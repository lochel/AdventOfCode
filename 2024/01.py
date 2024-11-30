#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split('   '))

  A = [int(line[0]) for line in lines]
  B = [int(line[1]) for line in lines]

  A.sort()
  B.sort()

  answer = sum(abs(a - b) for a, b in zip(A, B))
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split('   '))

  A = [int(line[0]) for line in lines]
  B = [int(line[1]) for line in lines]

  answer = sum(a * B.count(a) for a in A)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
