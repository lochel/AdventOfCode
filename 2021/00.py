#!../.env/bin/python3

import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else '00.in'
LINES = [line.strip() for line in open(input_file)]

# 1.
# ----------------------------------------
def problem1():
  answer = None
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = None
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
