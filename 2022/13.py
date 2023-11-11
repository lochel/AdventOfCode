#!../.env/bin/python3

from functools import cmp_to_key
from math import prod

from aoc import LINES, N

def parseList(line):
  i=0
  res = []
  while i < len(line):
    if line[i] == '[':
      child, j = parseList(line[i+1:])
      i += j+1
      res.append(child)
    elif line[i] == ']':
      return res, i+1
    elif line[i] == ',':
      i += 1
    elif line[i] != ',':
      number = ''
      while line[i] not in [',', ']', '[']:
        number = number + line[i]
        i += 1
      if number:
        res.append(int(number))
  return res, i


def cmp(lhs, rhs):
  if isinstance(lhs, int) and isinstance(rhs, int):
    if lhs == rhs:
      return 0
    if lhs < rhs:
      return 1
    return -1

  if isinstance(lhs, int):
    return cmp([lhs], rhs)

  if isinstance(rhs, int):
    return cmp(lhs, [rhs])

  for i in range(min(len(lhs), len(rhs))):
    res = cmp(lhs[i], rhs[i])
    if res != 0:
      return res
  if len(lhs) == len(rhs):
    return 0
  if len(lhs) < len(rhs):
    return 1
  return -1


# 1. What is the sum of the indices of those pairs?
# ----------------------------------------
def problem1():
  answer = 0
  index = 1
  for i in range(0, N, 3):
    lhs, _ = parseList(LINES[i])
    rhs, _ = parseList(LINES[i+1])
    if cmp(lhs, rhs) != -1:
      answer += index
    index += 1

  print(f'Answer 1: {answer}')


# 2. What is the decoder key for the distress signal?
# ----------------------------------------
def problem2():
  divider = ['[[2]]', '[[6]]']
  pks = []
  for d in divider:
    pkg, _ = parseList(d)
    pks.append(pkg)
  for d in LINES:
    if d:
      pkg, _ = parseList(d)
      pks.append(pkg)

  pks = sorted(pks, key=cmp_to_key(cmp), reverse=True)

  answer = prod([i+1 for i,pkg in enumerate(pks) if str(pkg[0]) in divider])
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
