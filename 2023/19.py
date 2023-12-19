#!../.env/bin/python3

import aoc

RULES = {}
for line in aoc.CHUNKS[0]:
  name, rest = line.split('{')
  rest = rest[:-1]
  cond = []
  default = None
  for c in rest.split(','):
    if '<' in c:
      x, r = c.split('<')
      y, z = r.split(':')
      cond.append((x, '<', int(y), z))
    elif '>' in c:
      x, r = c.split('>')
      y, z = r.split(':')
      cond.append((x, '>', int(y), z))
    else:
      default = c
  RULES[name] = (cond, default)

def accepted(xmas, label='in'):
  if label == 'A':
    return True
  elif label == 'R':
    return False

  conditions, default = RULES[label]
  for (x, op, y, z) in conditions:
    if op == '>' and xmas[x] > y:
      return accepted(xmas, z)
    elif op == '<' and xmas[x] < y:
      return accepted(xmas, z)

  return accepted(xmas, default)

def get_accepted_ranges(lb, ub, label='in'):
  if label == 'A':
    return [((lb['x'], ub['x']), (lb['m'], ub['m']), (lb['a'], ub['a']), (lb['s'], ub['s']))]
  elif label == 'R':
    return []

  new_lb = {'x': lb['x'], 'm': lb['m'], 'a': lb['a'], 's': lb['s']}
  new_ub = {'x': ub['x'], 'm': ub['m'], 'a': ub['a'], 's': ub['s']}

  conditions, default = RULES[label]
  for (x, op, y, z) in conditions:
    if op == '>' and ub[x] > y:
      lb[x] = y+1
      new_ub[x] = y
      return get_accepted_ranges(lb, ub, z) + get_accepted_ranges(new_lb, new_ub, label)
    elif op == '<' and lb[x] < y:
      ub[x] = y-1
      new_lb[x] = y
      return get_accepted_ranges(lb, ub, z) + get_accepted_ranges(new_lb, new_ub, label)

  return get_accepted_ranges(lb, ub, default)

# 1.
# ----------------------------------------
def problem1():
  answer = 0
  for line in aoc.CHUNKS[1]:
    line = line[1:-1]
    xmas = {}
    for v in line.split(','):
      name, value = v.split('=')
      xmas[name] = int(value)

    if accepted(xmas):
      answer += sum(xmas.values())

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  answer = 0
  lb = {'x': 1, 'm': 1, 'a': 1, 's': 1}
  ub = {'x': 4000, 'm': 4000, 'a': 4000, 's': 4000}
  for vx, vm, va, vs in get_accepted_ranges(lb, ub):
    answer += (vx[1]-vx[0]+1)*(vm[1]-vm[0]+1)*(va[1]-va[0]+1)*(vs[1]-vs[0]+1)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
