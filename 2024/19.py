#!../.env/bin/python3

import aoc


# 1.
# ----------------------------------------
def problem1():
  towels = aoc.CHUNKS[0][0].split(', ')
  patterns = aoc.CHUNKS[1]

  def test_pattern(pattern, towels):
    if not pattern:
      return 1

    for towel in towels:
      if pattern.startswith(towel):
        if test_pattern(pattern[len(towel):], towels) == 1:
          return 1

    return 0

  answer = 0
  for pattern in patterns:
    answer += test_pattern(pattern, towels)

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  towels = aoc.CHUNKS[0][0].split(', ')
  patterns = aoc.CHUNKS[1]

  lookup = {}

  def test_pattern(pattern, towels):
    if not pattern:
      return 1

    if pattern in lookup:
      return lookup[pattern]

    score = 0
    for towel in towels:
      if pattern.startswith(towel):
        score += test_pattern(pattern[len(towel):], towels)

    lookup[pattern] = score
    return score

  answer = 0
  for pattern in patterns:
    answer += test_pattern(pattern, towels)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
