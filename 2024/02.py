#!../.env/bin/python3

import aoc

def s1(line):
  y = line[0]-1
  for x in line:
    if x <= y:
      return False
    y = x
  return True

def s2(line):
  y = line[0]+1
  for x in line:
    if x >= y:
      return False
    y = x
  return True

def s3(line):
  y = line[0]+1
  for x in line:
    if not (1 <= abs(x-y) <= 3):
      return False
    y = x
  return True

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split(' '))
  lines = [[int(x) for x in line] for line in lines]

  answer = 0
  for line in lines:
    if (s1(line) or s2(line)) and s3(line):
      answer += 1

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split(' '))
  lines = [[int(x) for x in line] for line in lines]

  answer = 0
  for line in lines:
    for i,_ in enumerate(line):
      line_ = line[:i] + line[i+1:]
      if (s1(line_) or s2(line_)) and s3(line_):
        answer += 1
        break
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
