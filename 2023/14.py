#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  grid = aoc.parseLines(aoc.LINES, lambda line : list(line))

  for y in range(aoc.N):
    for x in range(aoc.M):
      if grid[y][x] == 'O':
        for z in range(y-1, -1, -1):
          if grid[z][x] != '.':
            break
          grid[z][x] = 'O'
          grid[z+1][x] = '.'

  answer = 0
  for x, y in aoc.Grid(grid):
    if grid[y][x] == 'O':
      answer += aoc.N-y
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  grid = aoc.parseLines(aoc.LINES, lambda line : list(line))

  loads = {}
  history = []
  while True:
    for y in range(aoc.N):
      for x in range(aoc.M):
        if grid[y][x] == 'O':
          for z in range(y-1, -1, -1):
            if grid[z][x] != '.':
              break
            grid[z][x] = 'O'
            grid[z+1][x] = '.'

    for x in range(aoc.M):
      for y in range(aoc.N):
        if grid[y][x] == 'O':
          for z in range(x-1, -1, -1):
            if grid[y][z] != '.':
              break
            grid[y][z] = 'O'
            grid[y][z+1] = '.'

    for y in range(aoc.N-1, -1, -1):
      for x in range(aoc.M):
        if grid[y][x] == 'O':
          for z in range(y+1, aoc.N, 1):
            if grid[z][x] != '.':
              break
            grid[z][x] = 'O'
            grid[z-1][x] = '.'

    for x in range(aoc.M-1, -1, -1):
      for y in range(aoc.N):
        if grid[y][x] == 'O':
          for z in range(x+1, aoc.M, 1):
            if grid[y][z] != '.':
              break
            grid[y][z] = 'O'
            grid[y][z-1] = '.'

    answer = 0
    Q = set()
    for x, y in aoc.Grid(grid):
      if grid[y][x] == 'O':
        answer += aoc.N-y
        Q.add((x, y))
    history.append(tuple(Q))

    if tuple(Q) not in loads:
      loads[tuple(Q)] = answer
    else:
      i = [j for j,x in enumerate(history) if x == tuple(Q)]
      print('  * Cycle starts after', i[0], 'steps')
      print('  * Cycle length:', i[1] - i[0])
      step = i[0] + (1000000000 - len(history)) % (i[1] - i[0])
      answer = loads[history[step]]
      print(f'Answer 2: {answer}')
      return

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
