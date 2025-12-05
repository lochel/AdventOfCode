#!../.env/bin/python3

import aoc


# 1.
# ----------------------------------------
def problem1():
  ranges = aoc.CHUNKS[0]
  ids = aoc.CHUNKS[1]
  ranges = aoc.parseLines(ranges, lambda line: tuple(map(int, line.split('-'))))
  ids = aoc.parseLines(ids, int)

  answer = 0
  for i in ids:
    for (low, high) in ranges:
      if i >= low and i <= high:
        answer += 1
        break

  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  ranges = aoc.CHUNKS[0]
  ranges = aoc.parseLines(ranges, lambda line: tuple(map(int, line.split('-'))))

  ranges.sort(key=lambda x: x[0])
  answer = 0
  last = -1
  for low, high in ranges:
    if low <= last:
      answer += max(high - last, 0)
      last = max(high, last)
    else:
      answer += high - low + 1
      last = high

  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
