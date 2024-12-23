#!../.env/bin/python3

from collections import defaultdict, deque
from functools import cmp_to_key
from itertools import combinations
from tqdm import tqdm
from math import prod

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split('-'))

  computers = set()
  network = defaultdict(set)
  for a,b in lines:
    computers.add(a)
    computers.add(b)
    network[a].add(b)
    network[b].add(a)

  groups = set()
  for a,b,c in tqdm(combinations(computers, 3)):
    if b in network[a] and b in network[c] and c in network[a] and c in network[b] and a in network[b] and a in network[c]:
      a,b,c = sorted([a,b,c])
      groups.add((a,b,c))

  answer = 0
  for a,b,c in groups:
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
      answer += 1

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split('-'))

  computers = set()
  network = defaultdict(set)
  for a,b in lines:
    computers.add(a)
    computers.add(b)
    network[a].add(b)
    network[b].add(a)

  # Find fully connected group of omputers
  answer = ''
  for k,v in network.items():
    group = [k] + list(v)
    group = sorted(group)
    redo = True
    while redo:
      redo = False
      for a,b in combinations(group, 2):
        if a not in network[b] or b not in network[a]:
          group.remove(a)
          redo = True
          break

    if len(','.join(group)) > len(answer):
      answer = ','.join(group)

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
