#!../.env/bin/python3

from math import prod
import aoc


LINES = aoc.parseLines(lambda line : line.split())
N = aoc.N


# 1. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
# ----------------------------------------
def problem1():
  monkeys = []
  monkey = {'score': 0}
  for line in LINES:
    if len(line) == 0:
      continue
    elif line[0] == 'Monkey':
      monkey = {'score': 0}
    elif line[0] == 'Starting':
      monkey['items'] = [int(item.replace(',', '')) for item in line[2:]]
    elif line[0] == 'Operation:':
      monkey['operation'] = [line[4], line[5]]
    elif line[0] == 'Test:':
      monkey['test'] = int(line[3])
    elif line[0] == 'If' and line[1] == 'true:':
      monkey['true'] = int(line[5])
    elif line[0] == 'If' and line[1] == 'false:':
      monkey['false'] = int(line[5])
      monkeys.append(monkey)

  N = len(monkeys)
  for _ in range(20):
    for i in range(N):
      for _ in range(len(monkeys[i]['items'])):
        # Get item
        item = monkeys[i]['items'].pop(0)
        monkeys[i]['score'] += 1

        # Do operation
        rhs = item
        if monkeys[i]['operation'][1] != 'old':
          rhs = int(monkeys[i]['operation'][1])
        if monkeys[i]['operation'][0] == '*':
          item = item * rhs
        elif monkeys[i]['operation'][0] == '+':
          item = item + rhs
        else:
          assert False

        item = item // 3

        # Test item
        if item % monkeys[i]['test'] == 0:
          next = monkeys[i]['true']
        else:
          next = monkeys[i]['false']
        monkeys[next]['items'].append(item)
        #print(f'{item} -> {next}')

  score = [monkeys[i]['score'] for i in range(N)]
  score.sort(reverse=True)
  answer = score[0]*score[1]
  print(f'Answer 1: {answer}')


# 2. What is the level of monkey business after 10000 rounds?
# ----------------------------------------
def problem2():
  monkeys = []
  monkey = {'score': 0}
  for line in LINES:
    if len(line) == 0:
      continue
    elif line[0] == 'Monkey':
      monkey = {'score': 0}
    elif line[0] == 'Starting':
      monkey['items'] = [int(item.replace(',', '')) for item in line[2:]]
    elif line[0] == 'Operation:':
      monkey['operation'] = [line[4], line[5]]
    elif line[0] == 'Test:':
      monkey['test'] = int(line[3])
    elif line[0] == 'If' and line[1] == 'true:':
      monkey['true'] = int(line[5])
    elif line[0] == 'If' and line[1] == 'false:':
      monkey['false'] = int(line[5])
      monkeys.append(monkey)

  LCD = prod([monkey['test'] for monkey in monkeys])
  N = len(monkeys)
  for _ in range(10000):
    for i in range(N):
      for _ in range(len(monkeys[i]['items'])):
        # Get item
        item = monkeys[i]['items'].pop(0)
        monkeys[i]['score'] += 1

        # Do operation
        rhs = item
        if monkeys[i]['operation'][1] != 'old':
          rhs = int(monkeys[i]['operation'][1])
        if monkeys[i]['operation'][0] == '*':
          item = item * rhs
        elif monkeys[i]['operation'][0] == '+':
          item = item + rhs
        else:
          assert False

        item = item - (item // LCD) * LCD

        # Test item
        if item % monkeys[i]['test'] == 0:
          next = monkeys[i]['true']
        else:
          next = monkeys[i]['false']
        monkeys[next]['items'].append(item)
        #print(f'{item} -> {next}')

  score = [monkeys[i]['score'] for i in range(N)]
  score.sort(reverse=True)
  answer = score[0]*score[1]
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
