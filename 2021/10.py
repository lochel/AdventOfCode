#!../.env/bin/python3

import statistics
from collections import deque

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  answer = 0
  for line in lines:
    Q = deque()
    for c in line:
      if c in '([{<':
        Q.append(c)
      elif c == ')':
        if Q.pop() != '(':
          answer += 3
          break
      elif c == ']':
        if Q.pop() != '[':
          answer += 57
          break
      elif c == '}':
        if Q.pop() != '{':
          answer += 1197
          break
      elif c == '>':
        if Q.pop() != '<':
          answer += 25137
          break

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  POINTS = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
  }

  scores = []
  for line in lines:
    Q = deque()
    corrupted = False
    for c in line:
      if c in '([{<':
        Q.append(c)
      elif c == ')':
        if Q.pop() != '(':
          corrupted = True
          break
      elif c == ']':
        if Q.pop() != '[':
          corrupted = True
          break
      elif c == '}':
        if Q.pop() != '{':
          corrupted = True
          break
      elif c == '>':
        if Q.pop() != '<':
          corrupted = True
          break
    if not corrupted:
      score = 0
      for x in reversed(Q):
        score = score * 5 + POINTS[x]
      scores.append(score)
  answer = statistics.median(scores)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
