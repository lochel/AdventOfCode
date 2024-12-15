#!../.env/bin/python3

from collections import defaultdict, deque
from functools import cmp_to_key
from itertools import combinations
from math import prod

import aoc

def is_on_map(x, y, maxX, maxY):
  return x >= 0 and x < maxX and y >= 0 and y < maxY

# 1.
# ----------------------------------------
def problem1():
  map = [list(line) for line in aoc.CHUNKS[0]]
  moves = ''.join([line for line in aoc.CHUNKS[1]])

  X = len(map[0])
  Y = len(map)

  for x,y in aoc.Grid(map):
    if map[y][x] == '@':
      pos = (x, y)

  for move in moves:
    x,y = pos

    if move == '<':
      dx,dy = -1,0
    elif move == '>':
      dx,dy = 1,0
    elif move == '^':
      dx,dy = 0,-1
    elif move == 'v':
      dx,dy = 0,1

    can_move = False
    n = 1
    while True:
      if not is_on_map(x+dx*n, y+dy*n, X, Y):
        break
      if map[y+dy*n][x+dx*n] == '#':
        break
      if map[y+dy*n][x+dx*n] == '.':
        can_move = True
        break
      n += 1

    if can_move:
      for i in range(n, 0, -1):
        map[y+dy*i][x+dx*i] = map[y+dy*(i-1)][x+dx*(i-1)]
      map[y][x] = '.'
      pos = (x+dx, y+dy)

    #print(f'Move {move}')
    #aoc.printGrid(map, delimiter='')

  answer = 0
  for x,y in aoc.Grid(map):
    if map[y][x] == 'O':
      answer += 100*y + x
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  map = []
  for line in aoc.CHUNKS[0]:
    new_line = []
    for x in line:
      if x == '#':
        new_line.append('#')
        new_line.append('#')
      elif x == 'O':
        new_line.append('[')
        new_line.append(']')
      elif x == '.':
        new_line.append('.')
        new_line.append('.')
      elif x == '@':
        new_line.append('@')
        new_line.append('.')
    map.append(new_line)
  moves = ''.join([line for line in aoc.CHUNKS[1]])

  X = len(map[0])
  Y = len(map)

  for x,y in aoc.Grid(map):
    if map[y][x] == '@':
      pos = (x, y)

  for move in moves:
    x,y = pos

    if move in '<>':
      if move == '<':
        dx = -1
      elif move == '>':
        dx = 1
      else:
        print('Error <>')

      can_move = False
      n = 1
      while True:
        if not is_on_map(x+dx*n, y, X, Y):
          break
        if map[y][x+dx*n] == '#':
          break
        if map[y][x+dx*n] == '.':
          can_move = True
          break
        n += 1

      if can_move:
        for i in range(n, 0, -1):
          map[y][x+dx*i] = map[y][x+dx*(i-1)]
        map[y][x] = '.'
        pos = (x+dx, y)

    elif move in '^v':
      if move == '^':
        dy = -1
      elif move == 'v':
        dy = 1
      else:
        print('Error ^v')

      can_move = False
      n = [[x]]
      while True:
        if not all([is_on_map(xx, y+dy*len(n), X, Y) for xx in n[-1]]):
          break
        if any([map[y+dy*len(n)][xx] == '#' for xx in n[-1]]):
          break
        if all([map[y+dy*len(n)][xx] == '.' for xx in n[-1]]):
          can_move = True
          break
        new_line = [x for x in n[-1] if map[y+dy*(len(n))][x] != '.']
        for ll in n[-1]:
          if map[y+dy*len(n)][ll] == ']' and ll-1 not in n[-1]:
            new_line.append(ll-1)
          if map[y+dy*len(n)][ll] == '[' and ll+1 not in n[-1]:
            new_line.append(ll+1)
        n.append(new_line)

      if can_move:
        for i in range(len(n), 0, -1):
          for xx in n[i-1]:
            map[y+dy*i][xx] = map[y+dy*(i-1)][xx]
            map[y+dy*(i-1)][xx] = '.'
        pos = (x, y+dy)

    #print(f'Move {move}')
    #aoc.printGrid(map, delimiter='')

  answer = 0
  for x,y in aoc.Grid(map):
    if map[y][x] == '[':
      answer += 100*y + x
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
