#!../.env/bin/python3

import aoc

elves, calories = [], 0
for line in aoc.LINES:
  if line:
    calories += int(line)
  else:
    elves.append(calories)
    calories = 0

# 1. How many total Calories is that Elf carrying?
# ----------------------------------------
def problem1():
  answer = max(elves)
  print(f'Answer 1: {answer}')

# 2. How many Calories are those Elves carrying in total?
# ----------------------------------------
def problem2():
  elves.sort(reverse=True)
  answer = sum(elves[0:3])
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
