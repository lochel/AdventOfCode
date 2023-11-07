#!../.env/bin/python3

import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else '01.in'
LINES = [int(line.strip()) for line in open(input_file)]

# 1.
# ----------------------------------------
def problem1():
  answer = 0
  old = LINES[0]
  for x in LINES:
    if x > old:
      answer += 1
    old = x
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = 0
  old = sum(LINES[0:3])
  for x in range(3, len(LINES)+1):
    y = sum(LINES[x-3:x])
    if y > old:
      answer += 1
    old = y
  print(f'Answer 1: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
