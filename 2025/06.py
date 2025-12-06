#!../.env/bin/python3

import math
import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split())

  answer = 0
  for i in range(len(lines[0])):
    op = lines[-1][i]
    numbers = [int(line[i]) for line in lines[:-1]]
    answer += sum(numbers) if op == '+' else math.prod(numbers)

  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  M = max(len(line) for line in lines)
  for i,line in enumerate(lines):
    lines[i] = line.ljust(M, ' ')

  op = None
  answer = 0
  for i in range(M):
    if lines[-1][i] != ' ' and op is not None:
      answer += sum(numbers) if op == '+' else math.prod(numbers)

    if lines[-1][i] != ' ':
      op = lines[-1][i]
      numbers = []

    new_number = ''
    for line in lines[:-1]:
      if line[i] != ' ':
        new_number += line[i]
    if new_number:
      numbers.append(int(new_number))

  answer += sum(numbers) if op == '+' else math.prod(numbers)
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
