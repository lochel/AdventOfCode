#!../.env/bin/python3

from collections import deque

import aoc

def printNumbers(NUM, IND):
  print(','.join([str(NUM[i]) for i in IND]))

# 1. What is the sum of the three numbers that form the grove coordinates?
# ----------------------------------------
def problem1():
  aoc.parseLines(int)
  numbers = aoc.LINES
  indices = deque(list(range(aoc.N)))

  for k in range(aoc.N):
    while indices[0] != k:
      indices.append(indices.popleft())

    IND = indices.popleft()
    NUM = numbers[IND]
    for t in range(NUM % (aoc.N-1)):
      indices.append(indices.popleft())
    indices.append(IND)

  while numbers[indices[0]] != 0:
    indices.append(indices.popleft())

  print('Answer 1: ', numbers[indices[1000%aoc.N]] + numbers[indices[2000%aoc.N]] + numbers[indices[3000%aoc.N]])

# 2. What is the sum of the three numbers that form the grove coordinates?
# ----------------------------------------
def problem2():
  numbers = [x*811589153 for x in aoc.LINES]
  indices = deque(list(range(aoc.N)))

  for _ in range(10):
    for k in range(aoc.N):
      while indices[0] != k:
        indices.append(indices.popleft())

      IND = indices.popleft()
      NUM = numbers[IND]
      for t in range(NUM % (aoc.N-1)):
        indices.append(indices.popleft())
      indices.append(IND)

  while numbers[indices[0]] != 0:
    indices.append(indices.popleft())

  print('Answer 2: ', numbers[indices[1000%aoc.N]] + numbers[indices[2000%aoc.N]] + numbers[indices[3000%aoc.N]])

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
