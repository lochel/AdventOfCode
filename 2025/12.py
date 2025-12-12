#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  chunks = aoc.CHUNKS

  shapes = {}
  for chunk in aoc.CHUNKS[:-1]:
    index = int(chunk[0][:-1])
    shape = [list(x) for x in chunk[1:]]
    size = sum(1 for line in shape for c in line if c == '#')
    shapes[index] = size

  regions = []
  for line in aoc.CHUNKS[-1]:
    line = line.replace(':', '')
    line = line.replace('x', ' ')
    numbers = [int(x) for x in line.split(' ') if x]
    regions.append((numbers[0], numbers[1], numbers[2:]))

  answer = 0
  for region in regions:
    width = region[0]
    length = region[1]
    packages = []

    present_size = sum(count*shapes[idx] for idx,count in enumerate(region[2]))
    grid_size = width*length
    if present_size < grid_size:
      answer += 1

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