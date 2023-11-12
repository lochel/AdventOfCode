#!../.env/bin/python3

import aoc

aoc.parseLines(lambda line : line.split())

# 1. Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# ----------------------------------------
def problem1():
  cycle = [1]
  for line in aoc.LINES:
    x = cycle[-1]
    if line[0] == 'noop':
      cycle.append(x)
    elif line[0] == 'addx':
      cycle.append(x)
      cycle.append(x + int(line[1]))
  answer = sum([cycle[t-1]*t for t in [20, 60, 100, 140, 180, 220]])
  print(f'Answer 1: {answer}')

# 2. What eight capital letters appear on your CRT?
# ----------------------------------------
def problem2():
  cycle = [1]
  for line in aoc.LINES:
    x = cycle[-1]
    if line[0] == 'noop':
      cycle.append(x)
    elif line[0] == 'addx':
      cycle.append(x)
      cycle.append(x + int(line[1]))

  print(f'Answer 2:')
  row = 40*['?']
  for j,x in enumerate(cycle):
    i = j % 40
    row[i] = '#' if abs(x-i) < 2 else ' '
    if i == 39:
      print(''.join(row))
      row = 40*['#']

# --------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
