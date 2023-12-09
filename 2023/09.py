#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : [int(x) for x in line.split()])

  answer = 0
  for line in lines:
    row = line
    history = [row]
    while row and any(row):
      row = [row[i+1]-row[i] for i in range(len(row)-1)]
      history.append(row)
    delta = 0
    for row in reversed(history):
      delta+=row[-1]
    answer += delta

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : [int(x) for x in line.split()])

  answer = 0
  for line in lines:
    row = line
    history = [row]
    while row and any(row):
      row = [row[i+1]-row[i] for i in range(len(row)-1)]
      history.append(row)
    delta = 0
    for row in reversed(history):
      delta=row[0]-delta
    answer += delta

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
