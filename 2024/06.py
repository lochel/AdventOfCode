#!../.env/bin/python3

import aoc

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = [list(line) for line in lines]

  for x, y in aoc.Grid(lines):
    if lines[y][x] in '^v<>':
      start = (x, y)
      dir = lines[y][x]
      lines[y][x] = 'X'

  pos = start
  answer = 1

  while True:
    x, y = pos

    if dir == '^':
      next = (x, y-1)
    elif dir == 'v':
      next = (x, y+1)
    elif dir == '<':
      next = (x-1, y)
    elif dir == '>':
      next = (x+1, y)

    nx, ny = next
    if nx < 0 or nx >= len(lines[0]) or ny < 0 or ny >= len(lines):
      break

    if lines[ny][nx] == '#':
      if dir == '^':
        dir = '>'
      elif dir == '>':
        dir = 'v'
      elif dir == 'v':
        dir = '<'
      elif dir == '<':
        dir = '^'

    elif lines[ny][nx] in '.^':
      answer += 1
      lines[ny][nx] = 'X'
      pos = next

    elif lines[ny][nx] == 'X':
      pos = next

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = [list(line) for line in lines]

  for x, y in aoc.Grid(lines):
    if lines[y][x] in '^v<>':
      start_pos = (x, y)
      start_dir = lines[y][x]
      lines[y][x] = '.'


  answer = 0
  for ox, oy in aoc.Grid(lines):
    if lines[oy][ox] == '#' or (ox, oy) == start_pos:
      continue

    obackup = lines[oy][ox]
    lines[oy][ox] = '#'

    Q = set()
    pos = start_pos
    dir = start_dir

    while True:
      x, y = pos

      if (x, y, dir) in Q:
        answer += 1
        break
      Q.add((x, y, dir))

      if dir == '^':
        next = (x, y-1)
      elif dir == 'v':
        next = (x, y+1)
      elif dir == '<':
        next = (x-1, y)
      elif dir == '>':
        next = (x+1, y)

      nx, ny = next
      if nx < 0 or nx >= len(lines[0]) or ny < 0 or ny >= len(lines):
        break

      if lines[ny][nx] == '#':
        if dir == '^':
          dir = '>'
        elif dir == '>':
          dir = 'v'
        elif dir == 'v':
          dir = '<'
        elif dir == '<':
          dir = '^'
        continue

      if lines[ny][nx] in '.':
        pos = next

    lines[oy][ox] = obackup

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
