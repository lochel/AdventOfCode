#!../.env/bin/python3

from itertools import combinations

import aoc

def mirror(chunk, a, b, smudges):
  if b < a:
    return mirror(chunk, b, a, smudges)

  if a < 0 or b >= len(chunk):
    return smudges

  for z in range(len(chunk[0])):
    for x, y in zip(chunk[a][z], chunk[b][z]):
      if x != y:
        smudges += 1

  if smudges > 1:
    return smudges
  return mirror(chunk, a-1, b+1, smudges)

def mirror2(chunk, a, b, smudges):
  if b < a:
    return mirror2(chunk, b, a, smudges)

  if a < 0 or b >= len(chunk[0]):
    return smudges

  for z in range(len(chunk)):
    for x, y in zip(chunk[z][a], chunk[z][b]):
      if x != y:
        smudges += 1

  if smudges > 1:
    return smudges
  return mirror2(chunk, a-1, b+1, smudges)

# 1.
# ----------------------------------------
def problem1():
  H = 0
  V = 0
  for chunk in aoc.CHUNKS:
    for a,b in combinations(range(len(chunk)), 2):
      if abs(a-b) == 1 and 0 == mirror(chunk, a, b, 0):
        V += min(a, b) + 1

    for a,b in combinations(range(len(chunk[0])), 2):
      if abs(a-b) == 1 and 0 == mirror2(chunk, a, b, 0):
        H += min(a, b) + 1

  print(f'Answer 1: {H + 100*V}')

# 2.
# ----------------------------------------
def problem2():
  H = 0
  V = 0
  for chunk in aoc.CHUNKS:
    for a,b in combinations(range(len(chunk)), 2):
      if abs(a-b) == 1 and 1 == mirror(chunk, a, b, 0):
        V += min(a, b) + 1

    for a,b in combinations(range(len(chunk[0])), 2):
      if abs(a-b) == 1 and 1 == mirror2(chunk, a, b, 0):
        H += min(a, b) + 1

  print(f'Answer 2: {H + 100*V}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
