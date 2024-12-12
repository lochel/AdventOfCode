#!../.env/bin/python3

from collections import defaultdict, deque
from functools import cmp_to_key
from itertools import combinations
from math import prod

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES

  garden_plots = defaultdict(list)
  for x,y in aoc.Grid(lines):
    garden_plots[lines[y][x]].append((x,y))

  answer = 0
  for label,plots in garden_plots.items():
    regions = []
    for x,y in plots:
      plot = (x,y)

      neighbors = []
      for xn,yn in aoc.get_neighbors(x,y,False,True):
        for idx,region in enumerate(regions):
          if (xn,yn) in region:
            neighbors.append(idx)

      if len(neighbors) == 0:
        xx = set()
        xx.add(plot)
        regions.append(xx)
      elif len(neighbors) == 1:
        regions[neighbors[0]].add(plot)
      else:
        new_regions = []
        merged_region = set()
        merged_region.add(plot)
        for i,p in enumerate(regions):
          if i in neighbors:
            merged_region |= p
          else:
            new_regions.append(p)
        new_regions.append(merged_region)
        regions = new_regions

    for region in regions:
      area = 0
      perimeter = 0
      for x,y in region:
        area += 1
        neighbors = 0
        for xn,yn in aoc.get_neighbors(x,y,False,False):
          if (xn,yn) in region:
            neighbors += 1
        perimeter += 4-neighbors
      answer += area*perimeter

  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES

  garden_plots = defaultdict(list)
  for x,y in aoc.Grid(lines):
    garden_plots[lines[y][x]].append((x,y))

  answer = 0
  for label,plots in garden_plots.items():
    regions = []
    for x,y in plots:
      plot = (x,y)

      neighbors = []
      for xn,yn in aoc.get_neighbors(x,y,False,True):
        for idx,region in enumerate(regions):
          if (xn,yn) in region:
            neighbors.append(idx)

      if len(neighbors) == 0:
        xx = set()
        xx.add(plot)
        regions.append(xx)
      elif len(neighbors) == 1:
        regions[neighbors[0]].add(plot)
      else:
        new_regions = []
        merged_region = set()
        merged_region.add(plot)
        for i,p in enumerate(regions):
          if i in neighbors:
            merged_region |= p
          else:
            new_regions.append(p)
        new_regions.append(merged_region)
        regions = new_regions

    for region in regions:
      area = 0
      perimeter = 0
      for x,y in region:
        area += 1
        corners = 0
        if (x-1,y) not in region and (x,y-1) not in region:
          corners += 1
        if (x+1,y) not in region and (x,y-1) not in region:
          corners += 1
        if (x-1,y) not in region and (x,y+1) not in region:
          corners += 1
        if (x+1,y) not in region and (x,y+1) not in region:
          corners += 1
        if (x-1,y) in region and (x,y-1) in region and (x-1,y-1) not in region:
          corners += 1
        if (x+1,y) in region and (x,y-1) in region and (x+1,y-1) not in region:
          corners += 1
        if (x-1,y) in region and (x,y+1) in region and (x-1,y+1) not in region:
          corners += 1
        if (x+1,y) in region and (x,y+1) in region and (x+1,y+1) not in region:
          corners += 1
        perimeter += corners
      answer += area*perimeter

  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
