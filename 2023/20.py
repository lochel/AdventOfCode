#!../.env/bin/python3

import math
from collections import deque

import aoc

# 1.
# ----------------------------------------
def problem1():
  Broadcaster = []
  FlipFlop = {}
  Conjunction = {}
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

  low = 0
  high = 0

  for step in range(1000):
    Q = deque()
    for x in Broadcaster:
      Q.append((x, 'broadcaster', False))

    low += 1
    while Q:
      name, origin, pulse = Q.popleft()

      if pulse:
        high += 1
      else:
        low += 1

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

  answer = high*low
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  Broadcaster = []
  FlipFlop = {}
  Conjunction = {}
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

  low = 0
  high = 0

  ll = []
  if 'rx' in Broadcaster:
    ll.append('broadcaster')
  for k,(v, _) in FlipFlop.items():
    if 'rx' in v:
      ll.append(k)
  for k,(v, _) in Conjunction.items():
    if 'rx' in v:
      ll.append(k)

  lll = []
  for xx in ll:
    if xx in Broadcaster:
      lll.append('broadcaster')
    for k,(v, _) in FlipFlop.items():
      if xx in v:
        lll.append(k)
    for k,(v, _) in Conjunction.items():
      if xx in v:
        lll.append(k)

  step = 0
  qq = []
  while True:
    step += 1

    #for x in :
    #  print(Conjunction[x][1])

    Q = deque()
    for x in Broadcaster:
      Q.append((x, 'broadcaster', False))

    low += 1
    while Q:
      name, origin, pulse = Q.popleft()

      if name in lll and not pulse:
        lll = [l for l in lll if l != name]
        qq.append(step)
      if not lll:
        print(f'Answer 2: {math.lcm(*qq)}')
        return

      if pulse:
        high += 1
      else:
        low += 1

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

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
