#!../.env/bin/python3

import os.path
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else os.path.splitext(sys.argv[0])[0] + '.in'
LINES = [line.strip().split() for line in open(input_file)]
N = len(LINES)
print(f'input contains {N} lines')


# 1. Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# ----------------------------------------
def problem1(LINES):
  cycle = [1]
  for line in LINES:
    x = cycle[-1]
    if line[0] == 'noop':
      cycle.append(x)
    elif line[0] == 'addx':
      cycle.append(x)
      cycle.append(x + int(line[1]))
  return sum([cycle[t-1]*t for t in [20, 60, 100, 140, 180, 220]])


# 2. What eight capital letters appear on your CRT?
# ----------------------------------------
def problem2(LINES):
  cycle = [1]
  for line in LINES:
    x = cycle[-1]
    if line[0] == 'noop':
      cycle.append(x)
    elif line[0] == 'addx':
      cycle.append(x)
      cycle.append(x + int(line[1]))

  row = 40*['?']
  for j,x in enumerate(cycle):
    i = j % 40
    row[i] = '#' if abs(x-i) < 2 else ' '
    if i == 39:
      print(''.join(row))
      row = 40*['#']


# --------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {problem1(LINES)}')
  print(f'Answer 2: {problem2(LINES)}\n')
