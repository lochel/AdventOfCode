#!../.env/bin/python3


# 1.
# ----------------------------------------
def problem1():
  with open('06.in') as f:
    data = f.readlines()
  data = [line.strip().split() for line in data]

  lights = dict()
  for line in data:
    action = line[1] if line[0] == 'turn' else line[0]
    x1, y1 = map(int, line[-3].split(','))
    x2, y2 = map(int, line[-1].split(','))

    for x in range(x1, x2 + 1):
      for y in range(y1, y2 + 1):
        if action == 'on':
          lights[(x, y)] = True
        elif action == 'off':
          lights[(x, y)] = False
        elif action == 'toggle':
          lights[(x, y)] = not lights.get((x, y), False)

  answer = sum(1 for v in lights.values() if v)
  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  with open('06.in') as f:
    data = f.readlines()
  data = [line.strip().split() for line in data]

  lights = dict()
  for line in data:
    action = line[1] if line[0] == 'turn' else line[0]
    x1, y1 = map(int, line[-3].split(','))
    x2, y2 = map(int, line[-1].split(','))

    for x in range(x1, x2 + 1):
      for y in range(y1, y2 + 1):
        l = lights.get((x, y), 0)
        if action == 'on':
          lights[(x, y)] = l + 1
        elif action == 'off':
          lights[(x, y)] = max(0, l - 1)
        elif action == 'toggle':
          lights[(x, y)] = l + 2

  answer = sum(v for v in lights.values())
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()