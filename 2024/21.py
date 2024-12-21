#!../.env/bin/python3

from collections import defaultdict, deque
from functools import cmp_to_key, lru_cache
from itertools import combinations, permutations, product
from math import prod

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  #  +---+---+---+
  #  | 7 | 8 | 9 |
  #  +---+---+---+
  #  | 4 | 5 | 6 |
  #  +---+---+---+
  #  | 1 | 2 | 3 |
  #  +---+---+---+
  #      | 0 | A |
  #      +---+---+
  #
  #      +---+---+
  #      | ^ | A |
  #  +---+---+---+
  #  | < | v | > |
  #  +---+---+---+

  numeric_keypad = {
    '7': (0,0), '8': (1,0), '9': (2,0),
    '4': (0,1), '5': (1,1), '6': (2,1),
    '1': (0,2), '2': (1,2), '3': (2,2),
                '0': (1,3), 'A': (2,3)
  }
  directional_keypad = {
                 '^': (1, 0), 'A': (2, 0),
    '<': (0, 1), 'v': (1, 1), '>': (2, 1)
  }

  def get_all_paths(sequence, keypad):
    result = []
    x, y = keypad['A']
    for target in sequence:
      nx,ny = keypad[target]
      dx = nx - x
      dy = ny - y

      path = ''
      if dx > 0:
        path += '>' * dx
      if dy > 0:
        path += 'v' * dy
      if dy < 0:
        path += '^' * -dy
      if dx < 0:
        path += '<' * -dx

      all_paths = set([''.join(p) for p in permutations(path)])
      valid_paths = []
      for p in all_paths:
        _x,_y = x,y
        valid = True
        for step in p:
          if step == '>':
            _x += 1
          if step == '<':
            _x -= 1
          if step == '^':
            _y -= 1
          if step == 'v':
            _y += 1

          if (_x,_y) not in keypad.values():
            valid = False
            break
        if valid:
          valid_paths.append(p + 'A')

      result.append(valid_paths)
      x,y = nx,ny

    return [''.join(x) for x in product(*result)]

  def complexity(line):
    paths1 = get_all_paths(line, numeric_keypad)
    paths2 = []
    for path in paths1:
      paths2.extend(get_all_paths(path, directional_keypad))
    paths3 = []
    for path in paths2:
      paths3.extend(get_all_paths(path, directional_keypad))

    return min([len(x) for x in paths3]) * int(line[:-1])

  #assert complexity('029A') == 68 * 29
  #assert complexity('980A') == 60 * 980
  #assert complexity('179A') == 68 * 179
  #assert complexity('456A') == 64 * 456
  #assert complexity('379A') == 64 * 379

  answer = 0
  for line in lines:
    answer += complexity(line)

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = None
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
