#!../.env/bin/python3

from tqdm import tqdm
import aoc

def next_number(number):
  x = number * 64
  x = x ^ number
  x = x % 16777216

  y = x // 32
  y = y ^ x
  y = y % 16777216

  z = y * 2048
  z = z ^ y
  z = z % 16777216

  return z

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : int(line))

  answer = 0
  for number in lines:
    for _ in range(2000):
      number = next_number(number)
    answer += number
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : int(line))

  profits = []
  all_seq = set()
  for seed in tqdm(lines):
    profit = dict()
    x = seed
    diff = [100, 100, 100, 100]
    for _ in range(2000-1):
      y = next_number(x)
      diff = diff[1:] + [(y % 10) - (x % 10)]
      x = y
      if 100 not in diff and tuple(diff) not in profit:
        profit[tuple(diff)] = x % 10
        all_seq.add(tuple(diff))
    profits.append(profit)

  answer = 0
  for seq in tqdm(all_seq):
    bananas = 0
    for profit in profits:
      if seq in profit:
        bananas += profit[seq]
    answer = max(answer, bananas)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
