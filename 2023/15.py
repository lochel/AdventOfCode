#!../.env/bin/python3

import aoc

def hash(s):
  current = 0
  for x in s:
    current += ord(x)
    current *= 17
    current %= 256
  return current

# 1.
# ----------------------------------------
def problem1():
  steps = aoc.DATA.split(',')

  answer = sum([hash(step) for step in steps])
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  steps = aoc.DATA.split(',')
  boxes = [[] for _ in range(256)]

  for step in steps:
    if step[-1] == '-':
      label = step[:-1]
      ibox = hash(label)
      boxes[ibox] = [(l,f) for (l,f) in boxes[ibox] if l!=label]
    elif step[-2] == '=':
      label = step[:-2]
      focal = int(step[-1])
      ibox = hash(label)
      if label in [l for (l,_) in boxes[ibox]]:
        boxes[ibox] = [(l,focal) if l==label else (l,f) for (l,f) in boxes[ibox]]
      else:
        boxes[ibox].append((label, focal))
    else:
      print('Error')

  answer = 0
  for ibox,box in enumerate(boxes):
    for islot,(_,f) in enumerate(box):
      answer += (ibox+1)*(islot+1)*f
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
