#!../.env/bin/python3

from collections import defaultdict, deque
from functools import cmp_to_key
from itertools import combinations
from math import prod

import aoc


# 1.
# ----------------------------------------
def problem1():
  map = aoc.LINES

  for x,y in aoc.Grid(map):
    if map[y][x] == 'S':
      start = (x,y)
    elif map[y][x] == 'E':
      end = (x,y)

  dir = (1,0)

  TODO = deque([(start,dir,0)])
  solutions = []

  best_score = dict()

  while TODO:
    (x,y),(dx,dy),score = TODO.popleft()

    if (x,y) == end:
      solutions.append(score)
      continue

    if map[y+dy][x+dx] != '#':
      if ((x+dx,y+dy),(dx,dy)) not in best_score or (((x+dx,y+dy),(dx,dy)) in best_score and best_score[((x+dx,y+dy),(dx,dy))] > score+1):
        TODO.append(((x+dx,y+dy),(dx,dy),score+1))
        best_score[((x+dx,y+dy),(dx,dy))] = score+1

    if ((x,y),(dy,dx)) not in best_score or (((x,y),(dy,dx)) in best_score and best_score[((x,y),(dy,dx))] > score+1000):
      TODO.append(((x,y),(dy,dx),score+1000))
      best_score[((x,y),(dy,dx))] = score+1000
    if ((x,y),(-dy,-dx)) not in best_score or (((x,y),(-dy,-dx)) in best_score and best_score[((x,y),(-dy,-dx))] > score+1000):
      TODO.append(((x,y),(-dy,-dx),score+1000))
      best_score[((x,y),(-dy,-dx))] = score+1000

  answer = min(solutions)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  map = aoc.LINES

  for x,y in aoc.Grid(map):
    if map[y][x] == 'S':
      start = (x,y)
    elif map[y][x] == 'E':
      end = (x,y)

  dir = (1,0)

  TODO = deque([(start,dir,0,[start])])
  solutions = set()

  best_score = dict()

  while TODO:
    (x,y),(dx,dy),score,path = TODO.popleft()

    if (x,y) == end:
      if score == 88468:
        for p in path:
          solutions.add(p)
      continue

    if map[y+dy][x+dx] != '#':
      if ((x+dx,y+dy),(dx,dy)) not in best_score or (((x+dx,y+dy),(dx,dy)) in best_score and best_score[((x+dx,y+dy),(dx,dy))] >= score+1):
        new_path = [p for p in path]
        new_path.append((x+dx,y+dy))
        TODO.append(((x+dx,y+dy),(dx,dy),score+1,new_path))
        best_score[((x+dx,y+dy),(dx,dy))] = score+1

    if ((x,y),(dy,dx)) not in best_score or (((x,y),(dy,dx)) in best_score and best_score[((x,y),(dy,dx))] >= score+1000):
      TODO.append(((x,y),(dy,dx),score+1000,path))
      best_score[((x,y),(dy,dx))] = score+1000
    if ((x,y),(-dy,-dx)) not in best_score or (((x,y),(-dy,-dx)) in best_score and best_score[((x,y),(-dy,-dx))] >= score+1000):
      TODO.append(((x,y),(-dy,-dx),score+1000,path))
      best_score[((x,y),(-dy,-dx))] = score+1000

  answer = len(solutions)
  #print(solutions)
  #for y in range(len(map)):
  #  for x in range(len(map[y])):
  #    if (x,y) in solutions:
  #      print('O',end='')
  #    else:
  #      print(map[y][x],end='')
  #  print()
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
