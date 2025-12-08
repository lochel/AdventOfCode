#!../.env/bin/python3

import aoc
from collections import defaultdict

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  boxes = aoc.parseLines(lines, lambda x: tuple(int(n) for n in x.split(',')))

  distances = []
  for i, (x, y, z) in enumerate(boxes):
    for j, (xx, yy, zz) in enumerate(boxes[:i]):
      d = abs(x - xx)**2 + abs(y - yy)**2 + abs(z - zz)**2
      distances.append((d, i, j))
  distances.sort()

  parent = {i: i for i in range(aoc.N)}

  def find_root(x):
    if x == parent[x]:
      return x
    parent[x] = find_root(parent[x])
    return parent[x]

  def union_sets(x, y):
    parent[find_root(x)] = find_root(y)

  count = 1000
  for _, i, j in distances:
    if find_root(i) != find_root(j):
      union_sets(i,j)

    count -= 1
    if count == 0:
      break

  component_sizes = defaultdict(int)
  for x in range(aoc.N):
    component_sizes[find_root(x)] += 1
  sorted_sizes = sorted(component_sizes.values())
  answer = sorted_sizes[-1]*sorted_sizes[-2]*sorted_sizes[-3]
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  boxes = aoc.parseLines(lines, lambda x: tuple(int(n) for n in x.split(',')))

  distances = []
  for i, (x, y, z) in enumerate(boxes):
    for j, (xx, yy, zz) in enumerate(boxes[:i]):
      d = abs(x - xx)**2 + abs(y - yy)**2 + abs(z - zz)**2
      distances.append((d, i, j))
  distances.sort()

  parent = {i: i for i in range(aoc.N)}

  def find_root(x):
    if x == parent[x]:
      return x
    parent[x] = find_root(parent[x])
    return parent[x]

  def union_sets(x, y):
    parent[find_root(x)] = find_root(y)

  connections = 0
  for _, i, j in distances:
    if find_root(i) != find_root(j):
      connections += 1
      if connections == aoc.N-1:
        break
      union_sets(i,j)

  answer = boxes[i][0]*boxes[j][0]
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
