#!../.env/bin/python3

import os.path
import sys
from collections import defaultdict

input_file = sys.argv[1] if len(sys.argv) > 1 else os.path.splitext(sys.argv[0])[0] + '.in'
LINES = [line.strip() for line in open(input_file)]
N = len(LINES)
print(f'input contains {N} lines')

# --------------------------------------
answer1 = 0
for line in LINES:
  l = len(line)//2
  item = [a for a in line[:l] if a in line[l:]][0]

  priority = ord(item) - ord('a') + 1
  if priority < 0:
    priority += 31 + 27
  answer1 += priority

answer2 = 0
for i in range(0, len(LINES), 3):
  badge = [a for a in LINES[i] if a in LINES[i+1] and a in LINES[i+2]][0]

  priority = ord(badge) - ord('a') + 1
  if priority < 0:
    priority += 31 + 27
  answer2 += priority

# --------------------------------------
# 1. What is the sum of the priorities of those item types?
# 2. What is the sum of the priorities of those item types?
print(f'Answer 1: {answer1}')
print(f'Answer 2: {answer2}')
