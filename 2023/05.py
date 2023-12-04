#!../.env/bin/python3

from collections import deque

import aoc

LINES = aoc.parseLines(aoc.LINES, lambda line : line.split(' '))

def findInMap(key, map):
  for [destination_range_start, source_range_start, range_length] in map:
    if source_range_start <= key < source_range_start+range_length:
      return destination_range_start + (key-source_range_start)
  return key

def mapRange(range, map):
  (rStart, rLength) = range

  if rLength == 1:
    return (findInMap(rStart, map), 1), None

  bound = 100000000000000000000000000000000
  for [destination_range_start, source_range_start, range_length] in map:
    if source_range_start > rStart and bound > source_range_start:
      bound = source_range_start
    if source_range_start <= rStart < source_range_start+range_length:
      l = min(rLength, source_range_start+range_length-rStart)
      mapped_range = (destination_range_start + (rStart-source_range_start), l)
      if l < rLength:
        return mapped_range, (rStart+l, rLength-l)
      return mapped_range, None

  l = min(bound, rStart+rLength) - rStart
  if rLength == l:
    return (rStart, l), None
  return (rStart, l), (rStart+l, rLength-l)

def findInMap2(key, map):
  Q = deque(key)
  result = []
  while Q:
    range = Q.pop()
    mapped, unmapped = mapRange(range, map)
    if unmapped:
      Q.append(unmapped)
    result.append(mapped)
  return result

seed_to_soil = []
for line in LINES[aoc.EMPTY[0]+2:aoc.EMPTY[1]]:
  line = [int(x) for x in line]
  seed_to_soil.append(line)

soil_to_fertilizer = []
for line in LINES[aoc.EMPTY[1]+2:aoc.EMPTY[2]]:
  line = [int(x) for x in line]
  soil_to_fertilizer.append(line)

fertilizer_to_water = []
for line in LINES[aoc.EMPTY[2]+2:aoc.EMPTY[3]]:
  line = [int(x) for x in line]
  fertilizer_to_water.append(line)

water_to_light = []
for line in LINES[aoc.EMPTY[3]+2:aoc.EMPTY[4]]:
  line = [int(x) for x in line]
  water_to_light.append(line)

light_to_temperature = []
for line in LINES[aoc.EMPTY[4]+2:aoc.EMPTY[5]]:
  line = [int(x) for x in line]
  light_to_temperature.append(line)

temperature_to_humidity = []
for line in LINES[aoc.EMPTY[5]+2:aoc.EMPTY[6]]:
  line = [int(x) for x in line]
  temperature_to_humidity.append(line)

humidity_to_location = []
for line in LINES[aoc.EMPTY[6]+2:]:
  line = [int(x) for x in line]
  humidity_to_location.append(line)

# 1.
# ----------------------------------------
def problem1():
  seeds = [int(x) for x in LINES[0][1:]]

  locations = []
  for seed in seeds:
    soil = findInMap(seed, seed_to_soil)
    fertilizer = findInMap(soil, soil_to_fertilizer)
    water = findInMap(fertilizer, fertilizer_to_water)
    light = findInMap(water, water_to_light)
    temperature = findInMap(light, light_to_temperature)
    humidity = findInMap(temperature, temperature_to_humidity)
    location = findInMap(humidity, humidity_to_location)
    locations.append(location)

  answer = min(locations)
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  seeds = [int(x) for x in LINES[0][1:]]

  seed_ranges = []
  for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i+1]))

  soil = findInMap2(seed_ranges, seed_to_soil)
  fertilizer = findInMap2(soil, soil_to_fertilizer)
  water = findInMap2(fertilizer, fertilizer_to_water)
  light = findInMap2(water, water_to_light)
  temperature = findInMap2(light, light_to_temperature)
  humidity = findInMap2(temperature, temperature_to_humidity)
  location = findInMap2(humidity, humidity_to_location)


  answer = min([a for (a, b) in location])
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
