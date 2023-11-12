#!../.env/bin/python3

import aoc


# 1.
# ----------------------------------------
def problem1():
  lines = aoc.parseLines(lambda line : line.split(' | ')[1].split())
  answer = 0
  for line in lines:
    for x in line:
      if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
        answer += 1
  print(f'Answer 1: {answer}')


# 2.
# ----------------------------------------
def problem2():
  # be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
  lines1 = aoc.parseLines(lambda line : line.split(' | ')[0].split())
  lines2 = aoc.parseLines(lambda line : line.split(' | ')[1].split())
  answer = 0

  for (a, [x1, x2, x3, x4]) in zip(lines1, lines2):
    map = {}

    #   1:      4:      7:      8:
    #  ....    ....    aaaa    aaaa
    # .    c  b    c  .    c  b    c
    # .    c  b    c  .    c  b    c
    #  ....    dddd    ....    dddd
    # .    f  .    f  .    f  e    f
    # .    f  .    f  .    f  e    f
    #  ....    ....    ....    gggg
    for x in a:
      x = ''.join(sorted(x))
      map[x] = '?'
      if len(x) == 2:
        map[x] = 1
        one = x
      elif len(x) == 3:
        map[x] = 7
      elif len(x) == 4:
        map[x] = 4
        four = x
      elif len(x) == 7:
        map[x] = 8


    #   2:      3:      5:
    #  aaaa    aaaa    aaaa
    # .    c  .    c  b    .
    # .    c  .    c  b    .
    #  dddd    dddd    dddd
    # e    .  .    f  .    f
    # e    .  .    f  .    f
    #  gggg    gggg    gggg
    for x in a:
      x = ''.join(sorted(x))
      if len(x) == 5:
        if all([a in x for a in one]):
          map[x] = 3
        elif len([a for a in four if a in x]) == 3:
          map[x] = 5
        else:
          map[x] = 2

    #   0:      6:      9:
    #  aaaa    aaaa    aaaa
    # b    c  b    .  b    c
    # b    c  b    .  b    c
    #  ....    dddd    dddd
    # e    f  e    f  .    f
    # e    f  e    f  .    f
    #  gggg    gggg    gggg
    for x in a:
      x = ''.join(sorted(x))
      if len(x) == 6:
        if all([digit in x for digit in four]):
          map[x] = 9
        elif all([digit in x for digit in one]):
          map[x] = 0
        else:
          map[x] = 6

    x1 = ''.join(sorted(x1))
    x2 = ''.join(sorted(x2))
    x3 = ''.join(sorted(x3))
    x4 = ''.join(sorted(x4))
    number = map[x1]*1000 + map[x2]*100 + map[x3]*10 + map[x4]
    answer += number
  print(f'Answer 2: {answer}')


# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
