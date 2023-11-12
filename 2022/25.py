#!../.env/bin/python3

import aoc

aoc.parseLines(lambda line : list(line))

def toDec(x):
  num = 0
  x.reverse()
  for i,c in enumerate(x):
    num += {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}[c] * 5**i
  return num

def toSNAFU(x):
  s = ""
  uber = 0
  while x:
    a = x % 5 + uber
    if a > 2:
      a -= 5
      uber = 1
    else:
      uber = 0
    s = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}[a] + s
    x = x//5
  return s

# 1. What SNAFU number do you supply to Bob's console?
# ----------------------------------------
def problem1():
  answer = 0
  for line in aoc.LINES:
    answer += toDec(line)

  print(f'Answer 1: {toSNAFU(answer)}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
