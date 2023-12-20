#!../.env/bin/python3

import math
from collections import deque

import aoc

Broadcaster = []
FlipFlop = {}
Conjunction = {}

def importFile():
  global Broadcaster

  Broadcaster.clear()
  FlipFlop.clear()
  Conjunction.clear()

  for line in aoc.LINES:
    if line[0] == '%':
      line = line[1:]
      name, destination_modules = line.split(' -> ')
      destination_modules = destination_modules.split(', ')
      FlipFlop[name] = (destination_modules, False)
    elif line[0] == '&':
      line = line[1:]
      name, destination_modules = line.split(' -> ')
      destination_modules = destination_modules.split(', ')
      Conjunction[name] = destination_modules
    elif line.startswith('broadcaster -> '):
      line = line.removeprefix('broadcaster -> ')
      Broadcaster = line.split(', ')

  for name, destinations in Conjunction.items():
    fg = {}
    if name in Broadcaster:
      fg['broadcaster'] = False
    for k,(v, _) in FlipFlop.items():
      if name in v:
        fg[k] = False
    for k,v in Conjunction.items():
      if name in v:
        fg[k] = False
    Conjunction[name] = (destinations, fg)

def pressButton(low, high, modules, steps, step):
  Q = deque()
  for x in Broadcaster:
    Q.append((x, 'broadcaster', False))

  # When you push the button, a single low pulse is sent directly to
  # the broadcaster module
  low += 1
  while Q:
    name, origin, pulse = Q.popleft()

    if pulse:
      high += 1
    else:
      low += 1

    if name in modules and not pulse:
      modules = [m for m in modules if m != name]
      steps.append(step)

    # Flip-flop modules (prefix %) are either on or off; they are
    # initially off. If a flip-flop module receives a high pulse, it
    # is ignored and nothing happens. However, if a flip-flop module
    # receives a low pulse, it flips between on and off. If it was
    # off, it turns on and sends a high pulse. If it was on, it turns
    # off and sends a low pulse.
    if not pulse and name in FlipFlop:
      (destination_modules, state) = FlipFlop[name]
      state = not state
      FlipFlop[name] = (destination_modules, state)
      for d in destination_modules:
        Q.append((d, name, state))

    # Conjunction modules (prefix &) remember the type of the most
    # recent pulse received from each of their connected input
    # modules; they initially default to remembering a low pulse for
    # each input. When a pulse is received, the conjunction module
    # first updates its memory for that input. Then, if it remembers
    # high pulses for all inputs, it sends a low pulse; otherwise, it
    # sends a high pulse.
    if name in Conjunction:
      (destination_modules, state) = Conjunction[name]
      state[origin] = pulse
      Conjunction[name] = (destination_modules, state)
      if all(state.values()):
        for d in destination_modules:
          Q.append((d, name, False))
      else:
        for d in destination_modules:
          Q.append((d, name, True))

  return low, high, modules, steps

# 1.
# ----------------------------------------
def problem1():
  importFile()

  low = 0
  high = 0
  for _ in range(1000):
    low, high, _, _ = pressButton(low, high, [], [], 0)

  answer = high*low
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  importFile()

  # This isn't a generic solution. A proper approach would be to
  # calculate cycles for all conjunctions.
  modules = [name for name,(destinations, _) in Conjunction.items() if 'rm' in destinations]

  step = 0
  steps = []
  while modules:
    step += 1
    _, _, modules, steps = pressButton(0, 0, modules, steps, step)

  answer = math.lcm(*steps)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
