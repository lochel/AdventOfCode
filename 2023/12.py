#!../.env/bin/python3

from itertools import combinations

import aoc

def solved(a, b, c):
  count = 0
  p = []
  for i,x in enumerate(a):
    inside = x == '#' or i in c
    if inside:
      count += 1
    elif count != 0:
      p.append(count)
      count = 0
  if count != 0:
    p.append(count)
  return p == b

Q = {}
def solved2(a, b, ia=0, ib=0, count=0):
  hash = (ia, ib)
  if count == 0 and hash in Q:
    return Q[hash]

  if ia == len(a):
    if ib == len(b) and count == 0:
      return 1
    elif ib+1 == len(b) and b[ib] == count:
      return 1
    return 0

  answer = 0
  if a[ia] in '.?':
    if count==0:
      answer += solved2(a, b, ia+1, ib, 0)
    elif ib<len(b) and b[ib] == count:
      answer += solved2(a, b, ia+1, ib+1, 0)

  if a[ia] in '#?':
    answer += solved2(a, b, ia+1, ib, count+1)

  if count == 0:
    Q[hash] = answer
  return answer

# 1.
# ----------------------------------------
def problem1():
  answer = 0
  for line in aoc.LINES:
    (a, b) = line.split()
    b = [int(x) for x in b.split(',')]
    question_marks = [i for i,x in enumerate(a) if x == '?']
    springs = [i for i,x in enumerate(a) if x == '#']
    for c in combinations(question_marks, sum(b) - len(springs)):
      answer += solved(a, b, c)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = 0
  for line in aoc.LINES:
    Q.clear()
    (a, b) = line.split()
    a = a + '?' + a + '?' + a + '?' + a + '?' + a
    b = [int(x) for x in b.split(',')] * 5
    answer += solved2(a, b)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
