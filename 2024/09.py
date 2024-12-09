#!../.env/bin/python3

import aoc
import itertools

# 1.
# ----------------------------------------
def problem1():
  data = aoc.DATA

  filesystem = []
  i = 0
  id = 0
  while i < len(data):
    x = int(data[i])
    if i % 2 == 0:
      for _ in range(x):
        filesystem.append(id)
      id += 1
    if i % 2 == 1:
      for _ in range(x):
        filesystem.append(None)
    i += 1

  print(filesystem)

  a = filesystem.index(None)
  i = len(filesystem) - 1
  while i > a:
    if filesystem[i] is not None:
      filesystem[a], filesystem[i] = filesystem[i], None
      a = filesystem.index(None)
    i -= 1

  print(filesystem)


  answer = 0
  for i,x in enumerate(filesystem):
    if x is not None:
      answer += i*x
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  data = aoc.DATA

  filesystem_id = []
  filesystem_size = []
  filesystem_start = []

  i = 0
  pos = 0
  while i < len(data):
    x = int(data[i])
    if i % 2 == 0 and x > 0:
      filesystem_id.append(i//2)
      filesystem_size.append(x)
      filesystem_start.append(pos)
      pos += x
    else:
      pos += x
    i += 1
  filesystem_start.append(pos)

  i = len(filesystem_id) - 1
  while i > 0:
    id = filesystem_id[i]
    length = filesystem_size[i]
    pos = filesystem_start[i]
    a = 0
    while a != i and filesystem_start[a+1] - filesystem_start[a] - filesystem_size[a] < length:
      a += 1

    if a == i:
      i -= 1
      continue

    filesystem_id = filesystem_id[:i] + filesystem_id[i+1:]
    filesystem_id.insert(a+1, id)

    filesystem_size = filesystem_size[:i] + filesystem_size[i+1:]
    filesystem_size.insert(a+1, length)

    filesystem_start = filesystem_start[:i] + filesystem_start[i+1:]
    filesystem_start.insert(a+1, pos)
    filesystem_start[a+1] = filesystem_start[a] + filesystem_size[a]

    #print(a, i, length)
    #print(filesystem_id)
    #print(filesystem_size)
    #print(filesystem_start)

    i -= 1

  answer = 0
  for i,x,p in zip(filesystem_id, filesystem_size, filesystem_start):
    for idx in range(x):
      answer += (p+idx)*i
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  #problem1()
  problem2()
