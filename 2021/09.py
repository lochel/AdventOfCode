#!../.env/bin/python3

import math
import sys

import aoc

sys.setrecursionlimit(10000)

# 1.
# ----------------------------------------
def problem1():
  answer = 0
  for x in range(aoc.M):
    for y in range(aoc.N):
      risk_point = True
      if x != 0 and aoc.LINES[y][x-1] <= aoc.LINES[y][x]:
          risk_point = False
      if x != aoc.M-1 and aoc.LINES[y][x+1] <= aoc.LINES[y][x]:
          risk_point = False
      if y != 0 and aoc.LINES[y-1][x] <= aoc.LINES[y][x]:
          risk_point = False
      if y != aoc.N-1 and aoc.LINES[y+1][x] <= aoc.LINES[y][x]:
          risk_point = False
      if risk_point:
         answer += int(aoc.LINES[y][x]) + 1
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def add_nei(Q, x, y):
  h = aoc.LINES[y][x]
  if (x,y) in Q or h == '9':
     return
  Q.add((x,y))
  if x != 0 and aoc.LINES[y][x-1] >= h:
      add_nei(Q, x-1, y)
  if x != aoc.M-1 and aoc.LINES[y][x+1] >= h:
      add_nei(Q, x+1, y)
  if y != 0 and aoc.LINES[y-1][x] >= h:
      add_nei(Q, x, y-1)
  if y != aoc.N-1 and aoc.LINES[y+1][x] >= h:
      add_nei(Q, x, y+1)


def problem2():
  basins = []
  for x in range(aoc.M):
    for y in range(aoc.N):
      risk_point = True
      if x != 0 and aoc.LINES[y][x-1] <= aoc.LINES[y][x]:
          risk_point = False
      if x != aoc.M-1 and aoc.LINES[y][x+1] <= aoc.LINES[y][x]:
          risk_point = False
      if y != 0 and aoc.LINES[y-1][x] <= aoc.LINES[y][x]:
          risk_point = False
      if y != aoc.N-1 and aoc.LINES[y+1][x] <= aoc.LINES[y][x]:
          risk_point = False
      if risk_point:
         Q = set()
         add_nei(Q, x, y)
         size = len(Q)
         basins.append(size)
  basins = sorted(basins, reverse=True)
  print(basins[:3])
  answer = math.prod(basins[:3])
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
