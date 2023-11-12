#!../.env/bin/python3

import aoc

LINES = aoc.LINES
EMPTY = aoc.EMPTY


# 1.
# --------------------------------------
def problem1():
  stacks = []
  for stack in range(9):
    stacks.append([LINES[h][stack*4+1] for h in range(EMPTY[0]-2, -1, -1) if LINES[h][stack*4+1] != ' '])

  for line in LINES[EMPTY[0]+1:]:
    line = line.split()
    a, b, c = int(line[1]), int(line[3]), int(line[5])

    for x in range(0, a):
      stacks[c-1].append(stacks[b-1].pop())

  answer = ''
  for l in stacks:
    answer += l[-1]
  return answer


# 2.
# --------------------------------------
def problem2():
  stacks = []
  for stack in range(9):
    stacks.append([LINES[h][stack*4+1] for h in range(EMPTY[0]-2, -1, -1) if LINES[h][stack*4+1] != ' '])

  for line in LINES[EMPTY[0]+1:]:
    line = line.split()
    a, b, c = int(line[1]), int(line[3]), int(line[5])

    tmp = []
    assert len(stacks[b-1]) >= a, f'{str(stacks[b-1])}, {line}'
    for x in range(0, a):
      tmp.append(stacks[b-1].pop())
    tmp.reverse()
    for x in tmp:
      stacks[c-1].append(x)

  answer = ''
  for l in stacks:
    answer += l[-1]
  return answer


# --------------------------------------
if __name__ == '__main__':
  answer1 = problem1()
  print(f'Answer 1: {answer1}')

  answer2 = problem2()
  print(f'Answer 2: {answer2}')
