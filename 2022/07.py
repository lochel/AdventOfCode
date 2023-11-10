#!../.env/bin/python3

import os.path
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else os.path.splitext(sys.argv[0])[0] + '.in'
LINES = [line.strip().split() for line in open(input_file)]
N = len(LINES)
print(f'input contains {N} lines')


# 1. What is the sum of the total sizes of those directories?
# --------------------------------------
def problem1():
  dirs = {}
  cur = []
  for line in LINES:
    if line[0] == '$':
      if line[1] == 'cd':
        if line[2] == '..':
          cur.pop()
          dirs['/'.join(cur)] = 0
        else:
          cur.append(line[2])
          dirs['/'.join(cur)] = 0

  cur = []
  d = []
  for line in LINES:
    if line[0] == '$':
      if line[1] == 'cd':
        if line[2] == '..':
          cur.pop()
        else:
          cur.append(line[2])
    elif line[0] != 'dir':
      if '/'.join(cur) in dirs:
        dirs['/'.join(cur)] += int(line[0])
      else:
        dirs['/'.join(cur)] = int(line[0])
    elif line[0] == 'dir':
      if '/'.join(cur) in dirs:
        h = '/'.join(cur) + ',' + line[1]
        if h not in d:
          d.append(h)

  for x in d:
    [a, b] = x.split(',')
    dirs[a] += dirs['/'.join([a,b])]

  answer = 0
  for x in dirs:
    if dirs[x] < 100000:
      answer += dirs[x]
  return answer

# 2. What is the total size of that directory?
# --------------------------------------
def sort_depth(e):
  return len(e.split('/'))

def problem2():
  dirs = {'/': 0}
  cur = []
  for line in LINES:
    if line[0] == '$':
      if line[1] == 'cd':
        if line[2] == '..':
          cur.pop()
          dirs['/'.join(cur)] = 0
        else:
          cur.append(line[2])
          dirs['/'.join(cur)] = 0

  cur = []
  d = []
  for line in LINES:
    if line[0] == '$':
      if line[1] == 'cd':
        if line[2] == '..':
          cur.pop()
        else:
          cur.append(line[2])
    elif line[0] != 'dir':
      if '/'.join(cur) in dirs:
        dirs['/'.join(cur)] += int(line[0])
      else:
        dirs['/'.join(cur)] = int(line[0])
    elif line[0] == 'dir':
      if '/'.join(cur) in dirs:
        h = '/'.join(cur) + ',' + line[1]
        if h not in d:
          d.append(h)

  d.sort(key=sort_depth, reverse=True)
  for x in d:
    [a, b] = x.split(',')
    dirs[a] += dirs['/'.join([a,b])]

  answer = 70000000
  free = 30000000 - (70000000 - dirs['/'])
  print('Need to free: ', free)

  for x in dirs:
    if dirs[x] >= free and answer > dirs[x]:
      answer = dirs[x]

  return answer


# --------------------------------------
if __name__ == '__main__':
  answer1 = problem1()
  print(f'Answer 1: {answer1}')

  answer2 = problem2()
  print(f'Answer 2: {answer2}')
