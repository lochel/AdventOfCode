#!../.env/bin/python3

import hashlib
import aoc

# 1. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
# ----------------------------------------
def problem1():
  key = aoc.DATA
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
  key = aoc.DATA
  num = 0
  while True:
    result = hashlib.md5(f'{key}{num}'.encode())
    if result.hexdigest().startswith('000000'):
      break
    num += 1
  print(f'Answer 2: {num}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
