#!../.env/bin/python3

import aoc


# 1.
# ----------------------------------------
def problem1():
  map = aoc.LINES
  map = [list(x) for x in map]

  for x,y in aoc.Grid(map):
    if map[y][x] == 'S':
      start = (x,y)
    if map[y][x] == 'E':
      end = (x,y)

  track = [start]
  x,y = start
  while map[y][x] != 'E':
    for nx,ny in aoc.get_neighbors(x, y, False, True):
      if map[ny][nx] != '#' and (nx,ny) not in track:
        track.append((nx,ny))
        x,y = nx,ny
        break

  c = 0
  count = 0
  for i in range(len(track)-2):
    x,y = track[i]
    if (x+2,y) in track:
      new_c = track.index((x+2,y))-i-2
      c = max(c, new_c)
      if new_c >= 100:
        count += 1
    if (x-2,y) in track:
      new_c = track.index((x-2,y))-i-2
      c = max(c, new_c)
      if new_c >= 100:
        count += 1
    if (x,y+2) in track:
      new_c = track.index((x,y+2))-i-2
      c = max(c, new_c)
      if new_c >= 100:
        count += 1
    if (x,y-2) in track:
      new_c = track.index((x,y-2))-i-2
      c = max(c, new_c)
      if new_c >= 100:
        count += 1
    if (x+1,y+1) in track:
      new_c = track.index((x+1,y+1))-i
      c = max(c, new_c-2)
      if new_c >= 100:
        count += 1
    if (x+1,y-1) in track:
      new_c = track.index((x+1,y-1))-i
      c = max(c, new_c-2)
      if new_c >= 100:
        count += 1
    if (x-1,y-1) in track:
      new_c = track.index((x-1,y-1))-i
      c = max(c, new_c-2)
      if new_c >= 100:
        count += 1
    if (x-1,y+1) in track:
      new_c = track.index((x-1,y+1))-i
      c = max(c, new_c-2)
      if new_c >= 100:
        count += 1

  print(len(track)-1)
  print(c)
  print(count)
  answer = count
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  map = aoc.LINES
  map = [list(x) for x in map]

  for x,y in aoc.Grid(map):
    if map[y][x] == 'S':
      start = (x,y)
    if map[y][x] == 'E':
      end = (x,y)

  track = [start]
  x,y = start
  while map[y][x] != 'E':
    for nx,ny in aoc.get_neighbors(x, y, False, True):
      if map[ny][nx] != '#' and (nx,ny) not in track:
        track.append((nx,ny))
        x,y = nx,ny
        break

  count = 0
  for i in range(len(track)-100):
    print(f'{i/(len(track)-2) * 100:.1f}\%', end='\r')
    x,y = track[i]
    for cx,cy in track[i+100:]:
      dist = abs(cx-x) + abs(cy-y)
      if dist > 20:
        continue
      c = track.index((cx,cy))-i-dist
      if c >= 100:
        count += 1

  answer = count
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  #problem1()
  problem2()
