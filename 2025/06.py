#!../.env/bin/python3

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split())

  answer = 0
  for i in range(len(lines[0])):
    op = lines[-1][i]
    value = 0 if op == '+' else 1
    for line in lines[:-1]:
      if op == '+':
        value += int(line[i])
      else:
        value *= int(line[i])
    answer += value

  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  M = max(len(line) for line in lines)
  for i in range(len(lines)):
    lines[i] = lines[i].ljust(M, ' ')
    print(f"'{lines[i]}'")

  op = None
  numbers = []
  answer = 0
  for i in range(M):
    if lines[-1][i] != ' ':
      if op is not None:
        value = 0 if op == '+' else 1
        for num in numbers:
          if op == '+':
            value += int(num)
          else:
            value *= int(num)
        answer += value
        print(numbers)
        print('Computed group with op', op, 'value', value)

      print('New group started at', i, 'with op', lines[-1][i])
      op = lines[-1][i]
      numbers = []
    value = ''
    for line in lines[:-1]:
      if line[i] != ' ':
        value += line[i]
    if value:
      print('Found number', value)
      numbers.append(int(value))

  value = 0 if op == '+' else 1
  for num in numbers:
    if op == '+':
      value += int(num)
    else:
      value *= int(num)
  answer += value
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
