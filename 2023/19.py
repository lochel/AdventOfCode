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

def accepted(x, m, a, s):
  label = 'in'
  values = {'x': x, 'm': m, 'a': a, 's': s}

  while True:
    if label == 'A':
      return True
    elif label == 'R':
      return False

    conditions, default = RULES[label]
    label = default
    for (x, op, y, z) in conditions:
      if op == '>' and values[x] > y:
        label = z
        break
      elif op == '<' and values[x] < y:
        label = z
        break

def get_accepted_ranges(values, label='in'):
  x, m, a, s = values
  lb = {'x': x[0], 'm': m[0], 'a': a[0], 's': s[0]}
  ub = {'x': x[1], 'm': m[1], 'a': a[1], 's': s[1]}

  result = []
  while True:
    if label == 'A':
      result.append(((lb['x'], ub['x']), (lb['m'], ub['m']), (lb['a'], ub['a']), (lb['s'], ub['s'])))
      return result
    elif label == 'R':
      return result

    conditions, default = RULES[label]
    current_label = label
    label = default

    for (x, op, y, z) in conditions:
      if op == '>' and ub[x] > y:
        new_lb = {'x': lb['x'], 'm': lb['m'], 'a': lb['a'], 's': lb['s']}
        new_ub = {'x': ub['x'], 'm': ub['m'], 'a': ub['a'], 's': ub['s']}

        lb[x] = y+1
        new_ub[x] = y

        new_values = ((new_lb['x'], new_ub['x']), (new_lb['m'], new_ub['m']), (new_lb['a'], new_ub['a']), (new_lb['s'], new_ub['s']))
        result = result + get_accepted_ranges(new_values, current_label)

        current_label = label
        label = z
        break
      elif op == '<' and lb[x] < y:
        new_lb = {'x': lb['x'], 'm': lb['m'], 'a': lb['a'], 's': lb['s']}
        new_ub = {'x': ub['x'], 'm': ub['m'], 'a': ub['a'], 's': ub['s']}

        ub[x] = y-1
        new_lb[x] = y

        new_values = ((new_lb['x'], new_ub['x']), (new_lb['m'], new_ub['m']), (new_lb['a'], new_ub['a']), (new_lb['s'], new_ub['s']))
        result = result + get_accepted_ranges(new_values, current_label)

        current_label = label
        label = z
        break

# 1.
# ----------------------------------------
def problem1():
  answer = 0
  for line in aoc.CHUNKS[1]:
    line = line[1:-1]
    x, m, a, s = None, None, None, None
    for v in line.split(','):
      name, value = v.split('=')
      if name == 'x':
        x = int(value)
      elif name == 'm':
        m = int(value)
      elif name == 'a':
        a = int(value)
      elif name == 's':
        s = int(value)

    if accepted(x, m, a, s):
      answer += x+m+a+s

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  x = (1, 4000)
  m = (1, 4000)
  a = (1, 4000)
  s = (1, 4000)

  answer = 0
  for vx, vm, va, vs in get_accepted_ranges((x, m, a, s)):
    answer += (vx[1]-vx[0]+1)*(vm[1]-vm[0]+1)*(va[1]-va[0]+1)*(vs[1]-vs[0]+1)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
