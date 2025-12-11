#!../.env/bin/python3

import aoc
from functools import cache

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda x: x.split(' '))

  data = {}
  for line in lines:
    key = line[0][:-1]
    values = line[1:]
    data[key] = values

  Q = ['you']
  answer = 0
  while Q:
    node = Q.pop(0)
    if node == 'out':
      answer += 1
      continue
    for neighbor in data[node]:
      Q.append(neighbor)

  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda x: x.split(' '))

  data = {}
  for line in lines:
    key = line[0][:-1]
    values = line[1:]
    data[key] = values

  @cache
  def find_path(node, fft, dac):
    if node == 'out':
      return 1 if fft and dac else 0

    count = 0
    for neighbor in data[node]:
      n_fft = fft or (neighbor == 'fft')
      n_dac = dac or (neighbor == 'dac')
      count += find_path(neighbor, n_fft, n_dac)
    return count

  answer = find_path('svr', False, False)
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()