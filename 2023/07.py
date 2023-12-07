#!../.env/bin/python3

from collections import Counter, defaultdict
from functools import cmp_to_key

import aoc

def values(card, joker=False):
  return { '2': 2,
           '3': 3,
           '4': 4,
           '5': 5,
           '6': 6,
           '7': 7,
           '8': 8,
           '9': 9,
           'T': 10,
           'J': 1 if joker else 11,
           'Q': 12,
           'K': 13,
           'A': 14}[card]

def category(hand, joker=False):
  v = Counter(hand)

  if joker:
    J = v['J'] if 'J' in v else 0
    v['J'] = 0
  else:
    J = 0

  v = sorted(v.values(), reverse=True)

  if J+v[0] == 5:
    return 7
  elif J+v[0] == 4:
    return 6
  elif J+v[0] == 3 and v[1] == 2:
    return 5
  elif J+v[0] == 3:
    return 4
  elif J+v[0] == 2 and v[1] == 2:
    return 3
  elif J+v[0] == 2:
    return 2
  return 1

def compare(hand1, hand2, joker=False):
  hand1 = hand1[0]
  hand2 = hand2[0]
  for a,b in zip(list(hand1), list(hand2)):
    if values(a, joker) > values(b, joker):
      return 1
    elif values(a, joker) < values(b, joker):
      return -1
  return 0

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split(' '))

  HANDS = defaultdict(list)
  for hand, bid in lines:
    cat = category(hand)
    HANDS[cat].append((hand, bid))

  for cat, v in HANDS.items():
    HANDS[cat] = sorted(v, key=cmp_to_key(compare))

  answer = 0
  rank = 0
  for cat in [1, 2, 3, 4, 5, 6, 7]:
    for hand, bid in HANDS[cat]:
      rank += 1
      answer += int(bid) * rank
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  lines = aoc.parseLines(lines, lambda line : line.split(' '))

  HANDS = defaultdict(list)
  for hand, bid in lines:
    cat = category(hand, joker=True)
    HANDS[cat].append((hand, bid))

  for cat, v in HANDS.items():
    HANDS[cat] = sorted(v, key=cmp_to_key(lambda a,b : compare(a, b, joker=True)))

  answer = 0
  rank = 0
  for cat in [1, 2, 3, 4, 5, 6, 7]:
    for hand, bid in HANDS[cat]:
      rank += 1
      answer += int(bid) * rank
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
