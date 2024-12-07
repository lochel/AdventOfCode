#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  lines = aoc.parseLines(lines, lambda line : line.split(': '))

  answer = 0
  for line in lines:
    result = int(line[0])
    numbers = [int(x) for x in line[1].split(' ')]

    r = [numbers[0]]
    for i in numbers[1:]:
      r_old = r
      r = []
      for x in r_old:
        r.append(x + i)
        r.append(x * i)

    if result in r:
      answer += result

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  lines = aoc.parseLines(lines, lambda line : line.split(': '))

  answer = 0
  for line in lines:
    result = int(line[0])
    numbers = [int(x) for x in line[1].split(' ')]

    r = [numbers[0]]
    for i in numbers[1:]:
      r_old = r
      r = []
      for x in r_old:
        r.append(x + i)
        r.append(x * i)
        r.append(int(str(x) + str(i)))

    if result in r:
      answer += result

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
