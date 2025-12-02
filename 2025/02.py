#!../.env/bin/python3

import aoc


# 1.
# ----------------------------------------
def problem1():
  ranges = aoc.DATA.split(',')
  ranges = aoc.parseLines(ranges, lambda x : x.split('-'))

  answer = 0
  for a, b in ranges:
    for i in range(int(a), int(b) + 1):
      x = str(i)
      if x[:len(x)//2] == x[len(x)//2:]:
        answer += i

  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  ranges = aoc.DATA.split(',')
  ranges = aoc.parseLines(ranges, lambda x : x.split('-'))

  answer = 0
  for a, b in ranges:
    for i in range(int(a), int(b) + 1):
      x = str(i)
      n = len(x)

      for j in range(1, n//2+1):
        N = n//j
        if x == x[:j] * N:
          answer += i
          break

  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
