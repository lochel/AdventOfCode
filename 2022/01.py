#!../.env/bin/python3

import os.path
import sys
from collections import defaultdict

input_file = sys.argv[1] if len(sys.argv) > 1 else os.path.splitext(sys.argv[0])[0] + '.in'
LINES = [line.strip() for line in open(input_file)]
N = len(LINES)
print(f'input contains {N} lines')

# --------------------------------------
elves, calories = [], 0
for line in LINES:
  if line:
    calories += int(line)
  else:
    elves.append(calories)
    calories = 0

answer1 = max(elves)
elves.sort(reverse=True)
answer2 = sum(elves[0:3])

# --------------------------------------
# 1. How many total Calories is that Elf carrying?
# 2. How many Calories are those Elves carrying in total?
print(f'Answer 1: {answer1}')
print(f'Answer 2: {answer2}')
