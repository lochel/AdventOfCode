#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  for c in range(26):
    lines = aoc.replaceLines(lines, chr(c+ord('a')))

  answer = 0
  for line in lines:
    answer += int((line[0] + line[-1]))

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  lines = aoc.replaceLines(lines, 'one', 'on1ne')
  lines = aoc.replaceLines(lines, 'two', 'tw2wo')
  lines = aoc.replaceLines(lines, 'three', 'th3ee')
  lines = aoc.replaceLines(lines, 'four', 'fo4ur')
  lines = aoc.replaceLines(lines, 'five', 'fi5ve')
  lines = aoc.replaceLines(lines, 'six', 'si6ix')
  lines = aoc.replaceLines(lines, 'seven', 'se7en')
  lines = aoc.replaceLines(lines, 'eight', 'ei8ht')
  lines = aoc.replaceLines(lines, 'nine', 'ni9ne')

  for c in range(26):
    lines = aoc.replaceLines(lines, chr(c+ord('a')))

  answer = 0
  for line in lines:
    answer += int((line[0] + line[-1]))

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
