#!../.env/bin/python3

import math
import statistics
import sys
from collections import defaultdict, deque
from itertools import combinations
import copy

import aoc

def bigCave(name):
  return 'A' <= name[0] <= 'Z'

def smallCave(name):
  return not bigCave(name)

# 1.
# ----------------------------------------
def problem1():
  map = defaultdict(list)
  indices = {}
  i=0
  for line in aoc.LINES:
    a, b = line.split('-')
    map[a].append(b)
    map[b].append(a)
    if a not in indices:
      indices[a] = i
      i += 1
    if b not in indices:
      indices[b] = i
      i += 1

  paths = set()
  Q = deque([['start']])
  while Q:
    path = Q.pop()
    pos = path[-1]
    next = map[pos]
    if pos == 'end':
      paths.add(tuple(path))
      continue
    for n in next:
      if smallCave(n) and n in path:
        continue
      if n == 'start':
        continue
      new_path = copy.deepcopy(path)
      new_path.append(n)
      Q.append(new_path)

  answer = len(paths)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  map = defaultdict(list)
  indices = {}
  i=0
  for line in aoc.LINES:
    a, b = line.split('-')
    map[a].append(b)
    map[b].append(a)
    if a not in indices:
      indices[a] = i
      i += 1
    if b not in indices:
      indices[b] = i
      i += 1

  paths = set()
  Q = deque([(False, ['start'])])
  while Q:
    dv, path = Q.pop()
    pos = path[-1]
    next = map[pos]
    if pos == 'end':
      paths.add(tuple(path))
      continue
    for n in next:
      if smallCave(n) and n in path and dv:
        continue
      if n == 'start':
        continue
      new_path = copy.deepcopy(path)
      new_path.append(n)
      Q.append(((smallCave(n) and new_path.count(n) == 2) or dv, new_path))

  answer = len(paths)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
