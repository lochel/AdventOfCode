#!../.env/bin/python3

import aoc

def getXY(s):
  for ss in s.split(' '):
    if ss.startswith('X'):
      x = int(ss[1:-1])
    if ss.startswith('Y'):
      y = int(ss[1:])
  return (x,y)

def getXY2(s, offset=0):
  for ss in s.split(' '):
    if ss.startswith('X='):
      x = int(ss[2:-1])+offset
    if ss.startswith('Y='):
      y = int(ss[2:])+offset
  return (x,y)

# 1.
# ----------------------------------------
def problem1():
  answer = 0
  for chunk in aoc.CHUNKS:
    A = getXY(chunk[0])
    B = getXY(chunk[1])
    result = getXY2(chunk[2])

    b = (result[0]*A[1] - A[0]*result[1]) / (-A[0]*B[1] + B[0]*A[1])
    a = (result[1] - b*B[1]) / A[1]

    if a.is_integer() and b.is_integer():
      answer += int(a) * 3 + int(b)

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = 0
  for chunk in aoc.CHUNKS:
    A = getXY(chunk[0])
    B = getXY(chunk[1])
    result = getXY2(chunk[2], 10000000000000)

    b = (result[0]*A[1] - A[0]*result[1]) / (-A[0]*B[1] + B[0]*A[1])
    a = (result[1] - b*B[1]) / A[1]

    if a.is_integer() and b.is_integer():
      answer += int(a) * 3 + int(b)

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
