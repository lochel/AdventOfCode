#!../.env/bin/python3

import aoc


# 1.
# ----------------------------------------
def problem1():

  locks = set()
  keys = set()
  for unit in aoc.CHUNKS:
    new_key = []
    new_lock = []
    for x in range(len(unit[0])):
      y = 0
      while y < len(unit) and unit[y][x] == '#':
        y += 1
      new_lock.append(y-1)

      y = 0
      while y < len(unit) and unit[y][x] == '.':
        y += 1
      new_key.append(7-y-1)

    if max(new_lock) != -1:
      locks.add(tuple(new_lock))
    if min(new_key) != 6:
      keys.add(tuple(new_key))

  answer = 0
  for key in keys:
    for lock in locks:
      if all(a+b < 6 for a, b in zip(key, lock)):
        answer += 1
  print(f'Answer 1: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
