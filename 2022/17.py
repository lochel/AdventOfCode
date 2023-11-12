#!../.env/bin/python3

from aoc import LINES

SHAPE1 = [['#','#','#','#']]

SHAPE2 = [['.','#','.'],
          ['#','#','#'],
          ['.','#','.']]

SHAPE3 = [['.','.','#'],
          ['.','.','#'],
          ['#','#','#']]

SHAPE4 = [['#'],
          ['#'],
          ['#'],
          ['#']]

SHAPE5 = [['#','#'],
          ['#','#']]

SHAPES = [SHAPE1, SHAPE2, SHAPE3, SHAPE4, SHAPE5]


def printTower(tower):
  dump = tower.copy()
  dump.reverse()
  for idx,line in enumerate(dump):
    print(f'{len(dump)-idx-1:<7}', end='')
    row = ''.join(line)
    print(row)


def playTetris(number_of_rocks):
  tower = [7*['#']]
  rock_id = 0
  rock = SHAPES[rock_id].copy()
  rock.reverse()
  rock_pos = 2
  rock_width = max([len(x) for x in rock])
  rock_height = 4

  history = []
  data = []

  time = -1
  offset_h = 0
  offset_r = 0
  N = len(LINES[0])
  while rock_id+offset_r < number_of_rocks:
    time += 1
    stream = LINES[0][time%N]

    # push rock
    if stream == '<' and rock_pos > 0:
      test_ok = True
      for rid,line in enumerate(rock):
        if rid+rock_height < len(tower):
          for xid,tt in enumerate(line):
            if tt == '#' and tower[rid+rock_height][rock_pos+xid-1] == '#':
              test_ok = False
      if test_ok:
        rock_pos -= 1
        #print('   move to left')
    elif stream == '>' and rock_pos+rock_width < 7:
      test_ok = True
      for rid,line in enumerate(rock):
        if rid+rock_height < len(tower):
          for xid,tt in enumerate(line):
            if tt == '#' and tower[rid+rock_height][rock_pos+xid+1] == '#':
              test_ok = False
      if test_ok:
        rock_pos += 1
        #print('   move to right')

    # can we fall?
    test_ok = True
    for rid,line in enumerate(rock):
      if rid+rock_height <= len(tower):
        for xid,tt in enumerate(line):
          if tt == '#' and tower[rid+rock_height-1][xid+rock_pos] == '#':
            test_ok = False
    if test_ok:
      rock_height -= 1
      #print('   move down')
    else:
      #print('   stop - new rock')
      # put the new rock
      for rid,line in enumerate(rock):
        new_line = 7*['.']
        if rid+rock_height < len(tower):
          for xid,tt in enumerate(line):
            if tt == '#':
              tower[rid+rock_height][xid+rock_pos] = tt
        else:
          for xid,tt in enumerate(line):
            if tt == '#':
              new_line[xid+rock_pos] = tt
          tower.append(new_line)

      # Save state:
      sig = []
      for x in range(7):
        y = len(tower) - 1
        while tower[y][x] != '#':
          y -= 1
        sig.append(len(tower) - y - 1)
      sig.append(time%N)
      sig.append(rock_id % 5)

      # Cycle detected!
      if sig in history and offset_r == 0:
        t_old = history.index(sig)
        dr = rock_id-data[t_old][1]
        dh = len(tower)-data[t_old][0]
        cycles = (number_of_rocks-rock_id-1) // dr
        offset_h = dh * cycles
        offset_r = dr * cycles

      history.append(sig)
      data.append((len(tower), rock_id))

      # generate new rock
      rock_id += 1
      rock = SHAPES[rock_id % 5].copy()
      rock.reverse()
      rock_pos = 2
      rock_width = max([len(x) for x in rock])
      rock_height = len(tower) + 3

  #printTower(tower)
  return len(tower)-1+offset_h

# 1. How many units tall will the tower of rocks be after 2022 rocks have stopped falling?
# ----------------------------------------
def problem1():
  print(f'Answer 1: {playTetris(2022)}')

# 2. How tall will the tower be after 1000000000000 rocks have stopped?
# ----------------------------------------
def problem2():
  print(f'Answer 2: {playTetris(1000000000000)}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
