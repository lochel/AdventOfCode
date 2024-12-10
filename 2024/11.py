#!../.env/bin/python3

import aoc
from collections import defaultdict

# 1.
# ----------------------------------------
def problem1():
  stones = aoc.DATA.split(' ')

  for _ in range(25):
    i = 0
    while i < len(stones):
      if stones[i] == '0':
        stones[i] = '1'
        i += 1
      elif len(stones[i]) % 2 == 0:
        a, b = stones[i][:len(stones[i])//2], stones[i][len(stones[i])//2:]
        stones[i] = str(int(a))
        stones.insert(i+1, str(int(b)))
        i += 2
      else:
        stones[i] = str(2024 * int(stones[i]))
        i += 1

  answer = len(stones)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  stones = aoc.DATA.split(' ')

  count = defaultdict(int)
  for stone in stones:
    count[stone] += 1

  for blink in range(75):
    new_count = defaultdict(int)
    for s,c in count.items():
      if s == '0':
        new_count['1'] += c
      elif len(s) % 2 == 0:
        a, b = str(int(s[:len(s)//2])), str(int(s[len(s)//2:]))
        new_count[a] += c
        new_count[b] += c
      else:
        new_count[str(2024 * int(s))] += c
    count = new_count

  answer = sum(c for s,c in count.items())
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
