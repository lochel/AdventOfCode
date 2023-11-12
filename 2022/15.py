#!../.env/bin/python3

import aoc

aoc.replaceLines('Sensor at x=')
aoc.replaceLines(' y=')
aoc.replaceLines(': closest beacon is at x=', ',')
aoc.parseLines(lambda line : [int(x) for x in line.split(',')])

beacon = {}
minX, maxX = 0,0
for line in aoc.LINES:
  sX,sY,bX,bY = line
  beacon[(sX,sY)] = (bX,bY,abs(sX-bX)+abs(sY-bY))
  minX = min(minX, sX, bX)
  maxX = max(maxX, sY, bY)

# 1.
# ----------------------------------------
def problem1(y, minX, maxX):
  answer = 0
  x = minX
  while x <= maxX:
    hit = False
    skip = 1
    for s in beacon:
      sX, sY = s
      bX, bY, d = beacon[s]

      if sX == x and sY == y:
        hit = True
        #print(2, x, y)
        break
      elif bX == x and bY == y:
        hit = True
        #print(3, x, y)
        break
      elif abs(sX-x)+abs(sY-y) <= d:
        hit = True
        skip = max(d - abs(sX-x)-abs(sY-y), 1)
        #print(1, x, y, skip)
        break
    if not hit:
      answer += 1
      print('solution: ',x,y,x*4000000+y, flush=True)
      break
    x += skip

  return answer

# 2.
# ----------------------------------------
def problem2():
  mmm = 4000000
  for y in range(mmm+1):
    r = problem1(y, 0, mmm)

# ----------------------------------------
if __name__ == '__main__':
  problem2()
