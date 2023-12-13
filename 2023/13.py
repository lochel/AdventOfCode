#!../.env/bin/python3

import aoc

def mirror(chunk, a, b, smudges):
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
  answer = 0
  for chunk in aoc.CHUNKS:
    for a in range(len(chunk)-1):
      if 0 == mirror(chunk, a, a+1, 0):
        answer += 100*(a + 1)

    for a in range(len(chunk[0])-1):
      if 0 == mirror2(chunk, a, a+1, 0):
        answer += a + 1
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = 0
  for chunk in aoc.CHUNKS:
    for a in range(len(chunk)-1):
      if 1 == mirror(chunk, a, a+1, 0):
        answer += 100*(a + 1)

    for a in range(len(chunk[0])-1):
      if 1 == mirror2(chunk, a, a+1, 0):
        answer += a + 1
  print(f'Answer 1: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
