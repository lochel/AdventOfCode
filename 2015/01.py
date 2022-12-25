#!../.env/bin/python3

import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
LINES = [list(line.strip()) for line in open(input_file)]

# 1. To what floor do the instructions take Santa?
# ----------------------------------------
def problem1():
  floor = 0
  for idx,dir in enumerate(LINES[0]):
    if dir == '(': floor += 1
    elif dir == ')': floor -= 1
    else: assert False, dir
  print(f'Answer 1: {floor}')

# 2. What is the position of the character that causes Santa to first enter the basement?
# ----------------------------------------
def problem2():
  floor = 0
  for idx,dir in enumerate(LINES[0]):
    if dir == '(': floor += 1
    elif dir == ')': floor -= 1
    else: assert False, dir

    if floor == -1:
      print(f'Answer 2: {idx+1}')
      return

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
