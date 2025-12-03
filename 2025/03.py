#!../.env/bin/python3

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  answer = 0
  for line in lines:
    m = max(line[:-1])
    i = line.find(m)
    n = max(line[i+1:])
    answer += int(m+n)
  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  answer = 0
  for line in lines:
    res = ''
    start = 0
    for z in range(12):
      m = max(line[start:len(line)-(11-z)])
      i = line.find(m, start)
      res += m
      start = i+1
    answer += int(res)
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
