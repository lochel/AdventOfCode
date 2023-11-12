#!../.env/bin/python3

from aoc import LINES, N

# 1.
# --------------------------------------
def problem1():
  c = list(LINES[0])
  xx = c[:4]
  for i in range(4, len(c)+1):
    xx.pop(0)
    xx.append(c[i])
    if len(set(xx)) >=4 :
      return i+1

# 2.
# --------------------------------------
def problem2():
  c = list(LINES[0])
  xx = c[:14]
  for i in range(14, len(c)+1):
    xx.pop(0)
    xx.append(c[i])
    if len(set(xx)) >=14 :
      return i+1

# --------------------------------------
if __name__ == '__main__':
  print(f'Answer 1: {problem1()}')
  print(f'Answer 2: {problem2()}')
