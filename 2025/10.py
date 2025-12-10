#!../.env/bin/python3

from collections import deque
import aoc
import z3

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda x: x.split(' '))

  diagram = []
  buttons = []
  voltage = []
  for line in lines:
    diagram.append(line[0].strip('[]'))
    buttons.append([[int(y) for y in x] for x in [z.strip('()').split(',') for z in line[1:-1]]])
    voltage.append([int(x) for x in line[-1].strip('{}').split(',')])

  answer = 0

  for i in range(aoc.N):
    local_steps = 10000
    solution = diagram[i]

    Q = deque([(0, "."*len(solution))])
    S = set()
    while Q:
      steps, state = Q.popleft()
      if steps >= local_steps:
        continue
      if state in S:
        continue
      S.add(state)
      if state == solution:
        if steps < local_steps:
          local_steps = steps
        break

      for button in buttons[i]:
        new_state = list(state)
        for b in button:
          if new_state[b] == '.':
            new_state[b] = '#'
          else:
            new_state[b] = '.'
        Q.append((steps + 1, "".join(new_state)))
    answer += local_steps
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda x: x.split(' '))

  buttons = []
  voltages = []
  for line in lines:
    buttons.append([list(map(int, cell.strip('()').split(','))) for cell in line[1:-1]])
    voltages.append(list(map(int, line[-1].strip('{}').split(','))))

  answer = 0
  for b, v in zip(buttons, voltages):
    V = [z3.Int(f'b_{i}') for i in range(len(b))]
    o = z3.Optimize()
    o.minimize(z3.Sum(*V))

    for i, need in enumerate(v):
      o.add(z3.Sum(*[V[j] for j, btn in enumerate(b) if i in btn]) == need)
    for var in V:
      o.add(var >= 0)

    o.check()
    m = o.model()
    answer += sum(m.eval(var).as_long() for var in V)

  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()