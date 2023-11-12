#!../.env/bin/python3

import math
from collections import deque

import aoc

LINES = aoc.parseLines(lambda line : line.replace(':', '').split())
N = aoc.N


# 1.
# ----------------------------------------
def problem1():
  monkeys = {}
  numbers = {}
  for line in LINES:
    if len(line) == 4:
      monkeys[line[0]] = (line[1], line[2], line[3])
    elif len(line) == 2:
      numbers[line[0]] = int(line[1])

  Q = ['root']
  while Q:
    q = Q.pop()

    if q in numbers:
      continue

    a, op, b = monkeys[q]

    if a not in numbers:
      Q.append(q)
      Q.append(a)
      continue
    if b not in numbers:
      Q.append(q)
      Q.append(b)
      continue


    if op == '+':
      res = f'({numbers[a]} + {numbers[b]})'
    elif op == '-':
      res = f'({numbers[a]} - {numbers[b]})'
    elif op == '*':
      res = f'({numbers[a]} * {numbers[b]})'
    elif op == '/':
      res = f'({numbers[a]} / {numbers[b]})'
    else:
      assert False

    numbers[q] = res
    if q == 'root':
      break

  print(f"Answer 1: {numbers['root']}")
  print(f"          = {eval(numbers['root'])}")

# 2.
# ----------------------------------------
def problem2():
  monkeys = {}
  numbers = {}
  for line in LINES:
    if line[0] == 'humn':
      numbers[line[0]] = 'x'
    elif len(line) == 4:
      monkeys[line[0]] = (line[1], line[2], line[3])
    elif len(line) == 2:
      numbers[line[0]] = int(line[1])

  Q = ['root']
  while Q:
    q = Q.pop()

    if q in numbers:
      continue

    a, op, b = monkeys[q]

    if a not in numbers:
      Q.append(q)
      Q.append(a)
      continue
    if b not in numbers:
      Q.append(q)
      Q.append(b)
      continue


    if q == 'root':
      res = f'({numbers[a]} - {numbers[b]})'
    elif op == '+':
      res = f'({numbers[a]} + {numbers[b]})'
    elif op == '-':
      res = f'({numbers[a]} - {numbers[b]})'
    elif op == '*':
      res = f'({numbers[a]} * {numbers[b]})'
    elif op == '/':
      res = f'({numbers[a]} / {numbers[b]})'
    else:
      assert False

    numbers[q] = res
    if q == 'root':
      break

  x = 0
  y = eval(numbers['root'])

  step = 10000000000
  while y != 0:
    x += round(step)
    y0 = eval(numbers['root'])

    if y < 0 <= y0:
      step *= -0.9
    elif y0 < 0 <= y:
      step *= -0.9

    y = y0
    #print(f'{x=} | {y=}')

  print(f"Answer 2: {round(x)}")


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
