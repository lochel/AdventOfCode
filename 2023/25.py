#!../.env/bin/python3

from itertools import combinations

import networkx as nx

import aoc

#sys.setrecursionlimit(10000)

# 1.
# ----------------------------------------
def problem1():
  connections = set()
  nodes = set()
  for line in aoc.LINES:
    a, B = line.split(': ')
    for b in B.split():
      nodes.add(a)
      nodes.add(b)
      if (b, a) not in connections:
        connections.add((a, b))

  # https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.flow.minimum_cut.html
  G = nx.DiGraph()
  answer = None
  for (a, b) in connections:
    G.add_edge(a, b, capacity=1.0)
    G.add_edge(b, a, capacity=1.0)

  for (start, stop) in combinations(nodes, 2):
    cut_value, (reachable, non_reachable) = nx.minimum_cut(G, start, stop)
    if cut_value == 3:
      answer = len(reachable)*len(non_reachable)
      break

  print(f'Answer 1: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
