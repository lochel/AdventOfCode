#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.replaceLines(lines, 'Card')
  lines = aoc.replaceLines(lines, ':')
  lines = aoc.replaceLines(lines, '  ', ' ')
  lines = aoc.parseLines(lines, lambda line: line.lstrip())
  lines = aoc.parseLines(lines, lambda line: line + ' #')
  lines = aoc.parseLines(lines, lambda line : line.split(' '))

  answer = 0
  for line in lines:
    numbers = []
    my_numbers = []
    my = False
    for n in line[1:]:
      if n == '|':
        my = True
      elif n == '#':
        score = 0
        for m in my_numbers:
          if m in numbers:
            score += 1
        if score > 0:
          answer += 2 ** (score-1)
      elif my:
        my_numbers.append(int(n))
      else:
        numbers.append(int(n))
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.replaceLines(lines, 'Card')
  lines = aoc.replaceLines(lines, ':')
  lines = aoc.replaceLines(lines, '  ', ' ')
  lines = aoc.parseLines(lines, lambda line: line.lstrip())
  lines = aoc.parseLines(lines, lambda line: line + ' #')
  lines = aoc.parseLines(lines, lambda line : line.split(' '))

  matched_numbers = []
  copies = []
  for line in lines:
    numbers = []
    my_numbers = []
    my = False
    for n in line[1:]:
      if n == '|':
        my = True
      elif n == '#':
        score = 0
        for m in my_numbers:
          if m in numbers:
            score += 1
        matched_numbers.append(score)
        copies.append(1)
      elif my:
        my_numbers.append(int(n))
      else:
        numbers.append(int(n))

  for i,v in enumerate(matched_numbers):
    for j in range(v):
      copies[i+j+1] += copies[i]

  print(f'Answer 2: {sum(copies)}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
