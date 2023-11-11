#!../.env/bin/python3
import aoc
import time

LINES = [line.replace('Valve', '').replace('has flow rate=', ',').replace('; tunnels lead to valves', ',').replace(
    '; tunnel leads to valve', ',').replace(' ', '').strip().split(',') for line in aoc.LINES]

# Might be a good idea to sort the valves :)
UNORDERED_VALVES = []
for line in LINES:
    name, rate, neighbors = line[0], int(line[1]), line[2:]
    UNORDERED_VALVES.append((name, rate, neighbors))
ORDERED_VALVES = sorted(UNORDERED_VALVES, key=lambda x: x[1], reverse=True)

MAPPING = {}
NAMES = []
NEIGHBORS = []
RATES = []
VALVES = []
for name, rate, neighbors in ORDERED_VALVES:
    valve_id = len(MAPPING)
    MAPPING[name] = valve_id
    NAMES.append(name)
    NEIGHBORS.append(neighbors)
    RATES.append(rate)
    if rate > 0:
      VALVES.append(valve_id)
for i in range(len(NEIGHBORS)):
  NEIGHBORS[i] = [MAPPING[name] for name in NEIGHBORS[i]]

def calc_dist(A, B, visited):
  if A == B:
    return 0

  dist = 1e6
  for neighbor in NEIGHBORS[A]:
    if neighbor not in visited:
      new_visited = visited.copy()
      new_visited.add(neighbor)
      dist = min(dist, 1 + calc_dist(neighbor, B, new_visited))
  return dist


# Calculate the distance matrix beforehand
DIST = []
for valve_id_y in range(len(MAPPING)):
  row = []
  for valve_id_x in range(valve_id_y+1):
    row.append(calc_dist(valve_id_y, valve_id_x, set()))
  DIST.append(row)

def getDist(A, B):
  return DIST[A][B] if A > B else DIST[B][A]

# print distance matrix
print(f'   ', end='')
for valve_id in range(len(MAPPING)):
  print(f'{NAMES[valve_id]:>3}', end='')
print('')
for valve_id_y in range(len(MAPPING)):
  print(f'{NAMES[valve_id_y]:>3}', end='')
  for valve_id_x in range(len(MAPPING)):
    print(f'{getDist(valve_id_y, valve_id_x):>3}', end='')
  print('')


def upper_pressure_limit(open_valves, time_left):
  limit = 0
  for valve in open_valves:
    if time_left > 0:
      limit += time_left * RATES[valve]
      time_left -= 2
  return limit

def upper_pressure_limit2(open_valves, time_left_A, time_left_B):
  limit = 0
  for valve in open_valves:
    if time_left_A > time_left_B:
      if time_left_A > 0:
        limit += time_left_A * RATES[valve]
        time_left_A -= 2
    else:
      if time_left_B > 0:
        limit += time_left_B * RATES[valve]
        time_left_B -= 2
  return limit

memo_pressure = {}
def release_pressure(A, open_valves, time_left):
  if (A, tuple(open_valves), time_left) in memo_pressure:
    return memo_pressure[(A, tuple(open_valves), time_left)]

  pressure = 0
  for valve in open_valves:
    dist = getDist(A, valve)
    if dist < time_left:
      open_valves2 = [x for x in open_valves if x != valve]
      if RATES[valve]*(time_left-dist-1) + upper_pressure_limit(open_valves2, time_left-dist-1) > pressure:
        pressure = max(pressure, RATES[valve]*(time_left-dist-1) + release_pressure(valve, open_valves2, time_left-dist-1))

  memo_pressure[(A, tuple(open_valves), time_left)] = pressure
  return pressure


memo_release_pressure2 = {}
def release_pressure2(A, B, open_valves, time_left_A, time_left_B, iteration=0):
  key = (A, B, tuple(open_valves), time_left_A, time_left_B, iteration)
  if key in memo_release_pressure2:
    return memo_release_pressure2[key]

  pressure = 0
  for valve in open_valves:
    if time_left_A-getDist(A, valve) > time_left_B-getDist(B, valve):
      distA = getDist(A, valve)
      if distA < time_left_A:
        open_valves2 = [x for x in open_valves if x != valve]
        if RATES[valve]*(time_left_A-distA-1) + upper_pressure_limit2(open_valves2, time_left_A-distA-1, time_left_B) > pressure:
          pressure = max(pressure, RATES[valve]*(time_left_A-distA-1) + release_pressure2(valve, B, open_valves2, time_left_A-distA-1, time_left_B, iteration+1))
        #else:
        #  print(f'Skip permutations (A) at {iteration=}, {pressure}')
    else:
      distB = getDist(B, valve)
      if distB < time_left_B:
        open_valves2 = [x for x in open_valves if x != valve]
        if RATES[valve]*(time_left_B-distB-1) + upper_pressure_limit2(open_valves2, time_left_A, time_left_B-distB-1) > pressure:
          pressure = max(pressure, RATES[valve]*(time_left_B-distB-1) + release_pressure2(A, valve, open_valves2, time_left_A, time_left_B-distB-1, iteration+1))
        #else:
        #  print(f'Skip permutations (B) at {iteration=}, {pressure}')
    if iteration == 0:
      print(f'Guess: {pressure}', flush=True)

  memo_release_pressure2[key] = pressure
  return pressure


# 1. What is the most pressure you can release?
# ----------------------------------------
def problem1():
    answer = release_pressure(MAPPING['AA'], VALVES, 30)
    print(f'Answer 1: {answer}')


# 2. With you and an elephant working together for 26 minutes, what is the most pressure you could release?
# ----------------------------------------
def problem2():
    answer = release_pressure2(MAPPING['AA'], MAPPING['AA'], VALVES, 26, 26)
    print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
    t = time.time()
    problem1()
    problem2()
    elapsed = time.time() - t
    print(f'elapsed time: {elapsed*1000:.0f}ms')
