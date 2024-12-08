#!../.env/bin/python3

import aoc
import itertools

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  antennas_pos = dict()
  for x,y in aoc.Grid(lines):
    if lines[y][x] == '.':
      continue
    if lines[y][x] not in antennas_pos:
      antennas_pos[lines[y][x]] = [(x,y)]
    else:
      antennas_pos[lines[y][x]].append((x,y))


  antinodes = set()
  for k,v in antennas_pos.items():
    for a,b in itertools.combinations(v, 2):
      dx = abs(a[0] - b[0])
      dy = abs(a[1] - b[1])

      if a[0] < b[0] and a[1] < b[1]:
        n1 = (a[0] - dx, a[1] - dy)
        n2 = (b[0] + dx, b[1] + dy)
      elif a[0] > b[0] and a[1] < b[1]:
        n1 = (a[0] + dx, a[1] - dy)
        n2 = (b[0] - dx, b[1] + dy)
      elif a[0] < b[0] and a[1] > b[1]:
        n1 = (a[0] - dx, a[1] + dy)
        n2 = (b[0] + dx, b[1] - dy)
      elif a[0] > b[0] and a[1] > b[1]:
        n1 = (a[0] - dx, a[1] - dy)
        n2 = (b[0] + dx, b[1] + dy)
      else:
        print("Error")

      if 0<= n1[0] < aoc.M and 0<= n1[1] < aoc.N:
        antinodes.add(n1)
      if 0<= n2[0] < aoc.M and 0<= n2[1] < aoc.N:
        antinodes.add(n2)

  answer = len(antinodes)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  antennas_pos = dict()
  for x,y in aoc.Grid(lines):
    if lines[y][x] == '.':
      continue
    if lines[y][x] not in antennas_pos:
      antennas_pos[lines[y][x]] = [(x,y)]
    else:
      antennas_pos[lines[y][x]].append((x,y))


  antinodes = set()
  for k,v in antennas_pos.items():
    for a,b in itertools.combinations(v, 2):
      dx = a[0] - b[0]
      dy = a[1] - b[1]

      antinodes.add(a)
      antinodes.add(b)

      n = (a[0] + dx, a[1] + dy)
      while 0<= n[0] < aoc.M and 0<= n[1] < aoc.N:
        antinodes.add(n)
        n = (n[0] + dx, n[1] + dy)

      n = (a[0] - dx, a[1] - dy)
      while 0<= n[0] < aoc.M and 0<= n[1] < aoc.N:
        antinodes.add(n)
        n = (n[0] - dx, n[1] - dy)

  answer = len(antinodes)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
