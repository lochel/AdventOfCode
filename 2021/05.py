#!../.env/bin/python3

import aoc

# 1. At how many points do at least two lines overlap?
# --------------------------------------
def problem1():
  count = {}
  for line in aoc.LINES:
    [a, b] = line.split(' -> ')
    a = [int(i) for i in a.split(',')]
    b = [int(i) for i in b.split(',')]

    if a[0] == b[0]:
      for z in range(min(a[1], b[1]), max(a[1], b[1])+1):
        if (a[0], z) in count:
          count[(a[0], z)] += 1
        else:
          count[(a[0], z)] = 1
    elif a[1] == b[1]:
      for z in range(min(a[0], b[0]), max(a[0], b[0])+1):
        if (z, a[1]) in count:
          count[(z, a[1])] += 1
        else:
          count[(z, a[1])] = 1

  return len(list(filter(lambda score: score > 1, list(count.values()))))

# 2.
# --------------------------------------
def problem2():
  count = {}
  for line in aoc.LINES:
    [a, b] = line.split(' -> ')
    a = [int(i) for i in a.split(',')]
    b = [int(i) for i in b.split(',')]

    if a[0] == b[0]:
      for z in range(min(a[1], b[1]), max(a[1], b[1])+1):
        if (a[0], z) in count:
          count[(a[0], z)] += 1
        else:
          count[(a[0], z)] = 1
    elif a[1] == b[1]:
      for z in range(min(a[0], b[0]), max(a[0], b[0])+1):
        if (z, a[1]) in count:
          count[(z, a[1])] += 1
        else:
          count[(z, a[1])] = 1
    else: # diagonal
      dx = 1 if a[0] < b[0] else -1
      dy = 1 if a[1] < b[1] else -1
      for z in range(abs(a[0]-b[0])+1):
        if (a[0] + z*dx, a[1] + z*dy) in count:
          count[(a[0] + z*dx, a[1] + z*dy)] += 1
        else:
          count[(a[0] + z*dx, a[1] + z*dy)] = 1

  return len(list(filter(lambda score: score > 1, list(count.values()))))

# --------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {problem1()}')
  print(f'Answer 2: {problem2()}')
