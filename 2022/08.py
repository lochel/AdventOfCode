#!../.env/bin/python3

import aoc

aoc.parseLines(lambda line : [int(z) for z in list(line)])

# 1. How many trees are visible from outside the grid?
# --------------------------------------
def problem1():
  forest = {}
  y = 0
  for line in aoc.LINES:
    y += 1
    x = 0
    for z in line:
      x += 1
      forest[(x, y)] = z

  for x in range(2, len(aoc.LINES[0])):
    for y in range(2, aoc.N):
      if forest[(x, y)] <= max([forest[(a, y)] for a in range(1, x)]):
        if forest[(x, y)] <= max([forest[(a, y)] for a in range(aoc.N, x, -1)]):
          if forest[(x, y)] <= max([forest[(x, a)] for a in range(1, y)]):
            if forest[(x, y)] <= max([forest[(x, a)] for a in range(aoc.N, y, -1)]):
              forest[(x, y)] = -1

  trees = list(forest.values())
  return len(trees) - trees.count(-1)

# 2. What is the highest scenic score possible for any tree?
# --------------------------------------
def problem2():
  forest = {}
  for y,line in enumerate(aoc.LINES):
    for x,z in enumerate(line):
      forest[(x, y)] = z

  scores = []
  for y,_ in enumerate(aoc.LINES):
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
      for i in range(x+1, aoc.N):
        score_ += 1
        if forest[(i, y)] >= forest[(x, y)]:
          break
      score *= score_

      score_ = 0
      for i in range(y+1, aoc.N):
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
