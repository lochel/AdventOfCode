#!../.env/bin/python3

from collections import deque

from aoc import LINES, N

WIDTH = len(LINES[0])
HIGHT = len(LINES)

BLIZZARDS = []
for y,line in enumerate(LINES):
  for x,tile in enumerate(line):
    if tile in ['>', '<', '^', 'v']:
      BLIZZARDS.append((x,y,tile))

def getMapAtTime(time):
  map = set()
  for x,y,tile in BLIZZARDS:
    if tile == '<':
      x = (x-time)
      while x < 1:
        x += WIDTH-2
    elif tile == '>':
      x = (x+time)
      while x > WIDTH-2:
        x -= WIDTH-2
    elif tile == '^':
      y = (y-time)
      while y < 1:
        y += HIGHT-2
    elif tile == 'v':
      y = (y+time)
      while y > HIGHT-2:
        y -= HIGHT-2
    map.add((x,y))
  return map

def printMap(map):
  for y in range(HIGHT):
    for x in range(WIDTH):
      if (x,y) in map:
        print('*', end='')
      else:
        print('.', end='')
    print('')

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

LCM = lcm(WIDTH-2, HIGHT-2)

MAP = []
for x in range(LCM):
  MAP.append(getMapAtTime(x))

def solve(start, end, time):
  #print(f'{WIDTH} x {HIGHT} (lcm {LCM})')
  best = 1e8
  (x, y) = start
  Q = deque([(x, y, time)])
  P = set()
  while Q:
    (x, y, time) = Q.popleft()

    if (x,y) == start:
      ##print('START')
      pass
    elif (x,y) == end:
      #print('END')
      best = min(best, time)
      #print(f'goal reached: {time} steps (best {best})')
      return best
      #continue
    elif not 1 <= x <= WIDTH-2:
      #print('wall |')
      continue
    elif not 1 <= y <= HIGHT-2:
      #print('wall -')
      continue
    elif (x,y) in MAP[time%LCM]:
      #print('blizzard')
      continue

    if (x, y, time%LCM) in P:
      #print('cache')
      continue
    else:
      P.add((x, y, time%LCM))

    Q.append((x,    y, time+1))
    Q.append((x-1,  y, time+1))
    Q.append((x,  y-1, time+1))
    Q.append((x+1,  y, time+1))
    Q.append((x,  y+1, time+1))

  return best

# 1.
# ----------------------------------------
def problem1():
  answer = solve((1, 0), (WIDTH-2,HIGHT-1), 0)
  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  answer = solve((1, 0), (WIDTH-2,HIGHT-1), 0)
  answer = solve((WIDTH-2,HIGHT-1), (1, 0), answer)
  answer = solve((1, 0), (WIDTH-2,HIGHT-1), answer)
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
