#!../.env/bin/python3

import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else '02.in'
LINES = [line.strip().split('x') for line in open(input_file)]

# 1. How many total square feet of wrapping paper should they order?
# ----------------------------------------
def problem1():
  paper = 0
  for line in LINES:
    l, w, h = int(line[0]), int(line[1]), int(line[2])
    paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
  print(f'Answer 1: {paper}')

# 2. How many total feet of ribbon should they order?
# ----------------------------------------
def problem2():
  ribbon = 0
  for line in LINES:
    l, w, h = int(line[0]), int(line[1]), int(line[2])
    ribbon += l*w*h + 2*l+2*w+2*h - 2*max(l, w, h)
  print(f'Answer 2: {ribbon}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
