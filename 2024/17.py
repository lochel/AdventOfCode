#!../.env/bin/python3

from collections import defaultdict, deque
from functools import cmp_to_key
from itertools import combinations
from math import prod

import aoc

def run_program(A, B, C, Program):
  instruction_pointer = 0

  def get_combo(value):
    if value == 0: return 0
    if value == 1: return 1
    if value == 2: return 2
    if value == 3: return 3
    if value == 4: return A
    if value == 5: return B
    if value == 6: return C
    raise ValueError(f'Invalid combo {value}')

  out = []

  while True:
    opcode = Program[instruction_pointer]

    literal = Program[instruction_pointer + 1]
    combo = get_combo(Program[instruction_pointer + 1])

    if opcode == 0:
      # adv - A := A//2^<combo>
      A //= 2**combo
      instruction_pointer += 2
    elif opcode == 1:
      # bxl - B xor <literal>
      B ^= literal
      instruction_pointer += 2
    elif opcode == 2:
      # bst - B := <combo> % 8
      B = combo % 8
      instruction_pointer += 2
    elif opcode == 3:
      # jnz
      if A != 0:
        instruction_pointer = literal
      else:
        instruction_pointer += 2
    elif opcode == 4:
      # bxc
      B = B ^ C
      instruction_pointer += 2
    elif opcode == 5:
      # out
      out.append(combo%8)
      instruction_pointer += 2
    elif opcode == 6:
      # bdv
      B = A // 2**combo
      instruction_pointer += 2
    elif opcode == 7:
      # cdv
      C = A // 2**combo
      instruction_pointer += 2
    else:
      print(f'Unknown opcode: {opcode}')
      break

    if instruction_pointer >= len(Program):
      break

  return out


def run_program2(A, B, C, Program):
  ALL = False
  next = [256,134217472,256,360709888,256,1073741568,256,98896376,479917320]
  answer = -1 if ALL else 359493309
  while True:
    if ALL:
      answer += 1
    else:
      answer += next[0]
      next = next[1:] + [next[0]]

    A = answer
    instruction_pointer = 0

    def get_combo(value):
      if value == 0: return 0
      if value == 1: return 1
      if value == 2: return 2
      if value == 3: return 3
      if value == 4: return A
      if value == 5: return B
      if value == 6: return C
      raise ValueError(f'Invalid combo {value}')

    out = []

    while True:
      opcode = Program[instruction_pointer]

      literal = Program[instruction_pointer + 1]
      combo = get_combo(Program[instruction_pointer + 1])

      if opcode == 0:
        # adv
        A //= 2**combo
        instruction_pointer += 2
      elif opcode == 1:
        # bxl
        B ^= literal
        instruction_pointer += 2
      elif opcode == 2:
        # bst
        B = combo % 8
        instruction_pointer += 2
      elif opcode == 3:
        # jnz
        if A != 0:
          instruction_pointer = literal
        else:
          instruction_pointer += 2
      elif opcode == 4:
        # bxc
        B = B ^ C
        instruction_pointer += 2
      elif opcode == 5:
        # out
        out.append(combo%8)
        instruction_pointer += 2

        if out[-1] != Program[len(out)-1]:
          break

        if len(out) == 9:
          print(answer, len(out)-1)

        if len(out) == len(Program):
          return answer
      elif opcode == 6:
        # bdv
        B = A // 2**combo
        instruction_pointer += 2
      elif opcode == 7:
        # cdv
        C = A // 2**combo
        instruction_pointer += 2
      else:
        print(f'Unknown opcode: {opcode}')
        break

      if instruction_pointer >= len(Program):
        break

# 1.
# ----------------------------------------
def problem1():
  lines = aoc.LINES
  A = int(lines[0].split(': ')[1])
  B = int(lines[1].split(': ')[1])
  C = int(lines[2].split(': ')[1])
  Program = [int(x) for x in lines[-1].split(':')[1].split(',')]

  out = run_program(A, B, C, Program)

  answer = ','.join([str(x) for x in out])
  print(f'Answer 1: {answer}')

# 2.
# ----------------------------------------
def problem2():
  lines = aoc.LINES
  A = int(lines[0].split(': ')[1])
  B = int(lines[1].split(': ')[1])
  C = int(lines[2].split(': ')[1])
  Program = [int(x) for x in lines[-1].split(':')[1].split(',')]

  answer = run_program2(A, B, C, Program)
  print(f'Answer 2: {answer}')

# ----------------------------------------
if __name__ == '__main__':
  problem1()
  problem2()
