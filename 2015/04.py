#!../.env/bin/python3

import hashlib
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else '04.in'
LINES = [line.strip() for line in open(input_file)]

# 1. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
# ----------------------------------------
def problem1():
  key = LINES[0]
  num = 0
  while True:
    result = hashlib.md5(f'{key}{num}'.encode())
    if result.hexdigest().startswith('00000'):
      break
    num += 1
  print(f'Answer 1: {num}')

# 2. Now find one that starts with six zeroes.
# ----------------------------------------
def problem2():
  key = LINES[0]
  num = 0
  while True:
    result = hashlib.md5(f'{key}{num}'.encode())
    if result.hexdigest().startswith('000000'):
      break
    num += 1
  print(f'Answer 1: {num}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
