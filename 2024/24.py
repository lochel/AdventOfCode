#!../.env/bin/python3

from collections import defaultdict, deque
from functools import cmp_to_key
from itertools import combinations, product
from math import prod
from tqdm import tqdm

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.CHUNKS[0]
  values = {}
  for line in lines:
    n,v = line.split(': ')
    values[n] = bool(v=='1')

  n_x = len([1 for n,_ in values.items() if n.startswith('x')])
  n_y = len([1 for n,_ in values.items() if n.startswith('y')])

  instructions = []
  lines = aoc.CHUNKS[1]
  for line in lines:
    a,d = line.split(' -> ')
    a,b,c = a.split(' ')
    instructions.append((a,b,c,d))

  next_instructions = instructions
  while next_instructions:
    instructions = next_instructions
    next_instructions = []
    for a,b,c,d in instructions:
      if d in values:
        continue
      if a in values and c in values:
        if b == 'AND':
          values[d] = values[a] and values[c]
        elif b == 'OR':
          values[d] = values[a] or values[c]
        elif b == 'XOR':
          values[d] = values[a] ^ values[c]
        else:
          print("ERROR")
        continue
      next_instructions.append((a,b,c,d))

  bits = [(n,v) for n,v in values.items() if n.startswith('z')]
  bits = sorted(bits, key=lambda x: x[0], reverse=True)
  bits = ['1' if v else '0' for n,v in bits]
  bits = ''.join(bits)
  answer = int(bits, 2)

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.CHUNKS[1]
  graph = {}
  out = set()
  for line in lines:
    a,d = line.split(' -> ')
    a,b,c = a.split(' ')
    graph[d] = (a,b,c)
    out.add(d)

  def exp(label, nAND=0, nOR=0, nXOR=0, depth=0):
    if depth > 500:
      return -999999, -999999, -999999

    if label not in graph:
      return nAND, nOR, nXOR

    a,b,c = graph[label]
    if b == 'AND':
      nAND += 1
    if b == 'OR':
      nOR += 1
    if b == 'XOR':
      nXOR += 1

    nAND, nOR, nXOR = exp(a, nAND, nOR, nXOR, depth+1)
    nAND, nOR, nXOR = exp(c, nAND, nOR, nXOR, depth+1)
    return nAND, nOR, nXOR

  def score(debug=False):
    for i in range(45):
      signal = f'z{i:02}'
      _a, _b, _c = exp(signal)

      if debug:
        print(signal, _a, _b, _c)

      if i == 0 and _a != 0:
        return i, signal
      if i != 0 and _a != i*2-1:
        return i, signal

      if i == 0 and _b != 0:
        return i, signal
      if i != 0 and _b != i-1:
        return i, signal

      if _c != i+1:
        return i, signal

    return i, None


  best = -1

  #_swap = [('kdf', 'z23'),('ckj', 'z15'), ('fdv', 'dbp')]
  ##('z39', 'rpp')
  #for a,b in _swap:
  #  out.remove(a)
  #  out.remove(b)
  #for a,b in _swap:
  #  graph[a], graph[b] = graph[b], graph[a]
  #
  #for p1,p2 in combinations(out, 2):
  #  graph[p1], graph[p2] = graph[p2], graph[p1]
  #  s, label = score()
  #  if s > best:
  #    best = s
  #    print(best, label, (p1,p2))
  #  graph[p1], graph[p2] = graph[p2], graph[p1]

  answer = ','.join(sorted(['z39', 'rpp', 'kdf', 'z23', 'ckj', 'z15', 'fdv', 'dbp']))
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
