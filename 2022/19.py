#!../.env/bin/python3

import aoc

aoc.replaceLines('Blueprint')
aoc.replaceLines(': Each ore robot costs', ',')
aoc.replaceLines('ore. Each clay robot costs', ',')
aoc.replaceLines('ore. Each obsidian robot costs', ',')
aoc.replaceLines('clay. Each geode robot costs', ',')
aoc.replaceLines('ore and', ',')
aoc.replaceLines('obsidian.')
aoc.replaceLines(' ')
aoc.parseLines(lambda line : line.split(','))


def enough_money(money, costs):
  more = [1e6, 1e6, 1e6, 1e6]
  if costs[0] > 0:
    more[0] = money[0] - costs[0]
  if costs[1] > 0:
    more[1] = money[1] - costs[1]
  if costs[2] > 0:
    more[2] = money[2] - costs[2]
  if costs[3] > 0:
    more[3] = money[3] - costs[3]
  return min(more) == 0

# Blueprint 1:
#   Each ore robot costs 4 ore.
#   Each clay robot costs 2 ore.
#   Each obsidian robot costs 3 ore and 14 clay.
#   Each geode robot costs 2 ore and 7 obsidian.
BLUEPRINTS = []
for line in aoc.LINES:
  id, costs, clay, obsidian_a, obsidian_b, geode_a, geode_b = int(line[0]), int(
    line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6])
  BLUEPRINTS.append(((costs, 0, 0, 0), (clay, 0, 0, 0),
            (obsidian_a, obsidian_b, 0, 0), (geode_a, 0, geode_b, 0)))
  #print(BLUEPRINTS[-1])
  assert id == len(BLUEPRINTS)


def simRobot(id, time, robots, money):
  cost0 = BLUEPRINTS[id][0]
  cost1 = BLUEPRINTS[id][1]
  cost2 = BLUEPRINTS[id][2]
  cost3 = BLUEPRINTS[id][3]

  Q = [(time, robots, money)]
  history = set()

  best = 0
  while Q:
    sig = Q.pop()
    t, (r0, r1, r2, r3), (ore, clay, obsidian, geodes) = sig
    best = max(best, geodes)

    if t <= 0:
      continue

    limit_ore = max([cost0[0], cost1[0], cost2[0], cost3[0]])
    if r0 > limit_ore:
      r0 = limit_ore
    limit_clay = max([cost0[1], cost1[1], cost2[1], cost3[1]])
    if r1 > limit_clay:
      r1 = limit_clay
    limit_obsidian = max([cost0[2], cost1[2], cost2[2], cost3[2]])
    if r2 > limit_obsidian:
      r2 = limit_obsidian

    if ore > t*limit_ore - r0*(t-1):
      ore = t*limit_ore - r0*(t-1)
    if clay > t*limit_clay - r1*(t-1):
      clay = t*limit_clay - r1*(t-1)
    if obsidian > t*limit_obsidian - r2*(t-1):
      obsidian = t*limit_obsidian - r2*(t-1)

    sig = (t, (r0, r1, r2, r3), (ore, clay, obsidian, geodes))
    if sig in history:
      continue
    else:
      history.add(sig)

    Q.append((t-1, (r0, r1, r2, r3), (ore+r0, clay+r1, obsidian+r2, geodes+r3)))
    if ore >= cost0[0] and clay >= cost0[1] and obsidian >= cost0[2]:
      Q.append((t-1, (r0+1, r1, r2, r3), (ore-cost0[0]+r0, clay-cost0[1]+r1, obsidian-cost0[2]+r2, geodes-cost0[3]+r3)))
    if ore >= cost1[0] and clay >= cost1[1] and obsidian >= cost1[2]:
      Q.append((t-1, (r0, r1+1, r2, r3), (ore-cost1[0]+r0, clay-cost1[1]+r1, obsidian-cost1[2]+r2, geodes-cost1[3]+r3)))
    if ore >= cost2[0] and clay >= cost2[1] and obsidian >= cost2[2]:
      Q.append((t-1, (r0, r1, r2+1, r3), (ore-cost2[0]+r0, clay-cost2[1]+r1, obsidian-cost2[2]+r2, geodes-cost2[3]+r3)))
    if ore >= cost3[0] and clay >= cost3[1] and obsidian >= cost3[2]:
      Q.append((t-1, (r0, r1, r2, r3+1), (ore-cost3[0]+r0, clay-cost3[1]+r1, obsidian-cost3[2]+r2, geodes-cost3[3]+r3)))

  return best

# 1. What do you get if you add up the quality level of all of the blueprints in your list?
# ----------------------------------------
def problem1():
  answer = 0
  for id, blueprint in enumerate(BLUEPRINTS):
    geodes = simRobot(id, 24, (1, 0, 0, 0), (0, 0, 0, 0))
    answer += (id+1)*geodes

  print(f'Answer 1: {answer}')

# 2. What do you get if you multiply these numbers together?
# ----------------------------------------
def problem2():
  answer = 1
  answer *= simRobot(0, 32, (1, 0, 0, 0), (0, 0, 0, 0))
  answer *= simRobot(1, 32, (1, 0, 0, 0), (0, 0, 0, 0))
  answer *= simRobot(2, 32, (1, 0, 0, 0), (0, 0, 0, 0))
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
