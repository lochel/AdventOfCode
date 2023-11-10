#!../.env/bin/python3

import os.path
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else os.path.splitext(sys.argv[0])[0] + '.in'
LINES = [[int(z) for z in list(line.strip())] for line in open(input_file)]
N = len(LINES)
print(f'input contains {N} lines')


# 1. How many trees are visible from outside the grid?
# --------------------------------------
def problem1():
  forest = {}
  y = 0
  for line in LINES:
    y += 1
    x = 0
    for z in line:
      x += 1
      forest[(x, y)] = z

  for x in range(2, len(LINES[0])):
    for y in range(2, N):
      if forest[(x, y)] <= max([forest[(a, y)] for a in range(1, x)]):
        if forest[(x, y)] <= max([forest[(a, y)] for a in range(N, x, -1)]):
          if forest[(x, y)] <= max([forest[(x, a)] for a in range(1, y)]):
            if forest[(x, y)] <= max([forest[(x, a)] for a in range(N, y, -1)]):
              forest[(x, y)] = -1

  trees = list(forest.values())
  return len(trees) - trees.count(-1)


# 2. What is the highest scenic score possible for any tree?
# --------------------------------------
def problem2():
  forest = {}
  for y,line in enumerate(LINES):
    for x,z in enumerate(line):
      forest[(x, y)] = z

  scores = []
  for y,_ in enumerate(LINES):
    for x,_ in enumerate(line):
      score = 1
      score_ = 0
      for i in range(x-1, -1, -1):
        score_ += 1
        if forest[(i, y)] >= forest[(x, y)]:
          break
      score *= score_

      score_ = 0
      for i in range(y-1, -1, -1):
        score_ += 1
        if forest[(x, i)] >= forest[(x, y)]:
          break
      score *= score_

      score_ = 0
      for i in range(x+1, N):
        score_ += 1
        if forest[(i, y)] >= forest[(x, y)]:
          break
      score *= score_

      score_ = 0
      for i in range(y+1, N):
        score_ += 1
        if forest[(x, i)] >= forest[(x, y)]:
          break
      score *= score_
      scores.append(score)

  return max(scores)


# --------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {problem1()}')
  print(f'Answer 2: {problem2()}')
